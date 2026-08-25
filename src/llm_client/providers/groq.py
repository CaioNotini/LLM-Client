from groq import Groq, AuthenticationError, PermissionDeniedError, APIConnectionError, APITimeoutError, RateLimitError, BadRequestError, UnprocessableEntityError, NotFoundError, GroqError
from ..config import LLMConfig
from ..exceptions import LLMAPIError, LLMRateLimitError, LLMError, LLMConnectionError, LLMAuthenticationError
from .base import BaseProvider
from ..decorators import retry, rate_limit, log_execution


class GroqProvider(BaseProvider):

    def __init__(self, api_key: str):
        if not api_key:
            raise LLMError("API key is required for GroqProvider.")

        self.client = Groq(api_key=api_key)

    @log_execution
    @rate_limit(calls_per_sec=2)
    @retry(vezes=3)
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

        except AuthenticationError as e:
            raise LLMAuthenticationError(
                f"Authentication failed for Groq: {str(e)}"
            )

        except PermissionDeniedError as e:
            raise LLMAuthenticationError(
                f"Permission denied for Groq: {str(e)}"
            )

        except (APIConnectionError, APITimeoutError) as e:
            raise LLMConnectionError(
                f"Connection error with Groq: {str(e)}"
            )

        except RateLimitError as e:
            raise LLMRateLimitError(
                "Rate limit exceeded for Groq."
            )

        except (BadRequestError, UnprocessableEntityError, NotFoundError) as e:
            raise LLMAPIError(
                f"Invalid request to Groq: {str(e)}"
            )

        except GroqError as e:
            raise LLMAPIError(
                f"Error generating text with Groq: {str(e)}"
            )