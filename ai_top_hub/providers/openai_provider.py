from openai import OpenAI
from ai_top_hub.providers.base_provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """
    OpenAI implementation of the BaseLLMProvider.
    """

    def __init__(self, model: str = "gpt-4o-mini", api_key: str | None = None):
        super().__init__(provider_name="openai")

        if api_key:
            self._client = OpenAI(api_key=api_key)
        else:
            self._client = OpenAI()

        self._model = model

    def generate(self, prompt: str) -> str:
        """
        Generate response using OpenAI model.
        """

        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        try:
            response = self._client.chat.completions.create(
                model=self._model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt}
                ]
            )

            content: str | None = response.choices[0].message.content
            return content or ""

        except Exception as e:
            raise RuntimeError(
                f"[OpenAIProvider | model={self._model}] Generation failed: {str(e)}"
            )