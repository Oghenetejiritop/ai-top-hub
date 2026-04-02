from ai_top_hub.providers.base_provider import BaseLLMProvider
from ai_top_hub.providers.claude_provider import ClaudeProvider
from ai_top_hub.providers.openai_provider import OpenAIProvider


def get_llm_provider(provider: str) -> BaseLLMProvider:
    """
    Factory function to return the appropriate LLM provider instance.
    """

    provider = provider.lower().strip()

    match provider:
        case "claude":
            return ClaudeProvider()
        case "openai":
            return OpenAIProvider()
        case _:
            raise ValueError(f"Unsupported provider: {provider}")