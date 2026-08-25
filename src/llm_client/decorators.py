from functools import wraps
from .exceptions import LLMAuthenticationError, LLMRateLimitError, LLMConnectionError

import time

def retry(vezes = 3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ultimo_erro  = None
            for i in range(vezes):
                try:
                    return func(*args, **kwargs)
                except LLMAuthenticationError as e:
                    print(f"Erro: {e}. Erro de autenticação. Verifique sua chave de API.")
                    raise
                except (LLMConnectionError, LLMRateLimitError) as e:
                    ultimo_erro = e
                    espera = 1* (2 ** i) 
                    print(f"Erro: {e}. Tentando novamente...")
                    time.sleep(espera)
            raise Exception(f"Falha após {vezes} tentativas.") from ultimo_erro
        return wrapper
    return decorator

def rate_limit(calls_per_sec):
    intervalo_minimo = 1.0 / calls_per_sec
    ultimo = [0]
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            agora = time.time()
            tempo_passado = agora - ultimo[0]
            if tempo_passado < intervalo_minimo:
                time.sleep(intervalo_minimo - tempo_passado)
            ultimo[0] = time.time()
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            kwargs_seguros = kwargs.copy()
            args_seguros = list(args)
            if "api_key" in kwargs_seguros:
                kwargs_seguros["api_key"] = kwargs_seguros["api_key"][:4] + "..." + kwargs_seguros["api_key"][-4:]
            if len(args_seguros) > 1 and len(args_seguros[1]) > 20:
                args_seguros[1] = args_seguros[1][:20] + "..."
            inicio = time.perf_counter()
            print(f"Executando {func.__name__} com argumentos: {args_seguros[1:]} e {kwargs_seguros}")
            result = func(*args, **kwargs)
            fim = time.perf_counter()
            print(f"{func.__name__} retornou: {result} (Tempo de execução: {fim - inicio:.2f} segundos)")
            return result
        except Exception as e:
            print(f"Erro em {func.__name__}: {e}")
            raise
    return wrapper