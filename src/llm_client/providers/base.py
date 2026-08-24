from abc import ABC, abstractmethod

from ..config import LLMConfig

class BaseProvider(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, config: LLMConfig) -> str:
        """Send 'prompt' to the LLM and return the generated text."""
        raise NotImplementedError("This method should be implemented by subclasses.")
        
