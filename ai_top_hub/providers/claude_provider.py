from anthropic import Anthropic
from ai_top_hub.providers.base_provider import BaseLLMProvider


class ClaudeProvider(BaseLLMProvider):
    """
    Anthropic Claude implementation of the BaseLLMProvider.
    """

    def __init__(self, model: str = "claude-sonnet-4-6", api_key: str | None = None):
        super().__init__(provider_name="claude")

        if api_key:
            self._client = Anthropic(api_key=api_key)
        else:
            self._client = Anthropic()

        self._model = model

    def generate(self, prompt: str) -> str:
        """
        Generate response using Claude model.
        """

        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        try:
            response = self._client.messages.create(
                model=self._model,
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            content_blocks = response.content

            if content_blocks and len(content_blocks) > 0:
                text = content_blocks[0].text
                return text or ""

            return ""

        except Exception as e:
            raise RuntimeError(
                f"[ClaudeProvider | model={self._model}] Generation failed: {str(e)}"
            )