from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Base class for all LLM providers.
    Every provider (OpenAI, Claude, etc.) must inherit from this.
    """

    def __init__(self, provider_name: str):
        self._provider_name = provider_name

    def get_provider_name(self) -> str:
        """
        Returns the name of the provider.
        """
        return self._provider_name

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt (str): Input text prompt

        Returns:
            str: Model response
        """
        raise NotImplementedError("Each provider must implement the generate method.")
    
