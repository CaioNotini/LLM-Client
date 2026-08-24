from dataclasses import dataclass

@dataclass
class LLMConfig:
    provider: str
    model: str
    temperature: float = 0.7
    max_tokens: int = 500