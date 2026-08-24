from .config import LLMConfig
from .exceptions import LLMConfigError
from .providers.base import BaseProvider
from .providers.groq import GroqProvider


class LLMClient:

    providers: dict[str, type[BaseProvider]] = {
        "groq": GroqProvider,
    }

    def __init__(self, config: LLMConfig, api_key: str):
        self.config = config
        self.provider = self.resolve_provider(
            config.provider,
            api_key
        )

    def resolve_provider(
        self,
        name: str,
        api_key: str
    ) -> BaseProvider:

        provider_class = self.providers.get(name)

        if not provider_class:
            raise LLMConfigError(
                f"Unsupported provider: {name}"
            )

        return provider_class(api_key)

    def generate(self, prompt: str) -> str:
        return self.provider.generate_text(
            prompt,
            self.config
        )