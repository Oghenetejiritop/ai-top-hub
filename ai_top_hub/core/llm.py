from ai_top_hub.providers.base_provider import BaseLLMProvider
from ai_top_hub.providers.claude_provider import ClaudeProvider
from ai_top_hub.providers.openai_provider import OpenAIProvider


def create_llm(provider: str, **kwargs) -> BaseLLMProvider:
    """
    Returns an initialized LLM provider instance.
    """
    provider_class = get_llm_provider(provider)
    return provider_class(**kwargs)
 

def get_llm_provider(provider: str) -> type[BaseLLMProvider]:
    """
    Returns the LLM provider class (not instance).
    Allows user to initialize with custom parameters.
    """

    provider = provider.lower().strip()

    providers = {
        "claude": ClaudeProvider,
        "openai": OpenAIProvider,
    }

    if provider not in providers:
        raise ValueError(f"Unsupported provider: {provider}")

    return providers[provider]
