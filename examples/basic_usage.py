import os

from dotenv import load_dotenv

from llm_client import LLMClient, LLMConfig


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

config = LLMConfig(
    provider="groq",
    model="openai/gpt-oss-20b",
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

print(response)