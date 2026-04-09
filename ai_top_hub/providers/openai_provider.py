from openai import OpenAI
from ai_top_hub.providers.base_provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """
    OpenAI implementation of the BaseLLMProvider.
    """

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        max_tokens: int = 100,
        temperature: float = 0.5,
        top_p: float = 1.0,
        api_key: str | None = None
    ):
        super().__init__(provider_name="openai")

        self._client = OpenAI(api_key=api_key) if api_key else OpenAI()

        self._model = model
        self._max_tokens = max_tokens
        self._temperature = temperature
        self._top_p = top_p

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
                        "content": prompt
                    }
                ],
                max_tokens=self._max_tokens,
                temperature=self._temperature,
                top_p=self._top_p
            )

            content: str | None = response.choices[0].message.content
            return content or ""

        except Exception as e:
            raise RuntimeError(
                f"[OpenAIProvider | model={self._model}] Generation failed: {str(e)}"
            )