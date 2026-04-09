from anthropic import Anthropic
from ai_top_hub.providers.base_provider import BaseLLMProvider


class ClaudeProvider(BaseLLMProvider):
    """
    Anthropic Claude implementation of the BaseLLMProvider.
    """

    def __init__(
        self,
        model: str = "claude-sonnet-4-6",
        max_tokens: int = 1024,
        temperature: float = 0.5,
        top_p: float = 1.0,
        api_key: str | None = None
    ):
        super().__init__(provider_name="claude")

        self._client = Anthropic(api_key=api_key) if api_key else Anthropic()

        self._model = model
        self._max_tokens = max_tokens
        self._temperature = temperature
        self._top_p = top_p

    def generate(self, prompt: str) -> str:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        try:
            params = {
                "model": self._model,
                "max_tokens": self._max_tokens,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

        # Anthropic constraint: cannot use both temperature and top_p
            if self._temperature is not None:
                params["temperature"] = self._temperature
            elif self._top_p is not None:
                params["top_p"] = self._top_p

            response = self._client.messages.create(**params)

            content_blocks = response.content

            if content_blocks and len(content_blocks) > 0:
                text = content_blocks[0].text
                return text or ""

            return ""

        except Exception as e:
            raise RuntimeError(
                f"[ClaudeProvider | model={self._model}] Generation failed: {str(e)}"
            )
