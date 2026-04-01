from openai import OpenAI
from ai_top_hub.providers.base_provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """
    OpenAI implementation of the BaseLLMProvider.
    """

    def __init__(self, model: str = "gpt-4o-mini", api_key: str | None = None):
        super().__init__(provider_name="openai")

        # Use provided key or fallback to environment variable
        if api_key:
            self._client = OpenAI(api_key=api_key) 
        else:
            self._client = OpenAI() 

        self._model = model 

    def generate(self, prompt: str) -> str:
        """
        Generate response using OpenAI model.
        """
        try:
            response = self._client.chat.completions.create( 
                model=self._model, 
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            content = response.choices[0].message.content
            return content if content else ""

        except Exception as e:
            raise RuntimeError(f"OpenAI generation failed: {str(e)}")