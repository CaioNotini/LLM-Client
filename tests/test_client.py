import os

from llm_client.config import LLMConfig
from llm_client.client import LLMClient


def main():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set.")

    config = LLMConfig(
        provider="groq",
        model="llama-3.1-8b-instant",
        temperature=0.7,
        max_tokens=100
    )

    client = LLMClient(
        config=config,
        api_key=api_key
    )

    response = client.generate(
        "Explique em uma frase o que é uma API."
    )

    print("Resposta:")
    print(response)


if __name__ == "__main__":
    main()