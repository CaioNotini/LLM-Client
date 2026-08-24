# LLM Client

Wrapper reutilizável em Python para integração com APIs de Large Language Models (LLMs).

O projeto fornece uma interface comum para diferentes providers, permitindo reutilizar a mesma estrutura em outros projetos sem depender diretamente da implementação de cada API.

## Funcionalidades

- Configuração de modelos através de `LLMConfig`;
- Interface unificada através de `LLMClient`;
- Abstração de providers com `BaseProvider`;
- Tratamento de erros personalizado;
- Estrutura preparada para adicionar providers.

## Arquitetura

```text
LLMClient
    |
    v
BaseProvider
    |
    +---- GroqProvider
    |
    +---- Outros providers
```

O `LLMClient` é responsável pela interface utilizada pela aplicação, enquanto cada `Provider` encapsula os detalhes específicos da API utilizada.

## Estrutura

```text
LLM-Client/
├── examples/
│   └── basic_usage.py
├── src/
│   └── llm_client/
│       ├── client.py
│       ├── config.py
│       ├── exceptions.py
│       └── providers/
│           ├── base.py
│           └── groq.py
├── tests/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/CaioNotini/LLM-Client.git
cd LLM-Client
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -e .
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```bash
GROQ_API_KEY=sua_api_key
```

A API key não deve ser adicionada ao Git.

## Uso

Um exemplo completo está disponível em:

```text
examples/basic_usage.py
```

Exemplo:

```python
config = LLMConfig(
    provider="groq",
    model="seu-modelo",
    temperature=0.7,
    max_tokens=100
)

client = LLMClient(
    config=config,
    api_key=api_key
)

response = client.generate("Pergunta exemplo.")

print(response)
```

## Testes

Execute os testes com:

```bash
pytest
```

Para executar o exemplo:

```bash
python examples/basic_usage.py
```
