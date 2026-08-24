from groq import Groq

from ..config import LLMConfig
from ..exceptions import LLMAPIError, LLMRateLimitError, LLMError

from .base import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(self, api_key: str):
        if not api_key:
            raise LLMError("API key is required for GroqProvider.")

        self.client = Groq(api_key=api_key)

    def generate_text(self, prompt: str, config: LLMConfig) -> str:
        try:
            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=config.temperature,
                max_tokens=config.max_tokens
            )

            return response.choices[0].message.content

        except Exception as e:
            if "rate limit" in str(e).lower():
                raise LLMRateLimitError(
                    "Rate limit exceeded for Groq."
                )

            raise LLMAPIError(
                f"Error generating text with Groq: {str(e)}"
            )