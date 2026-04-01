from ai_top_hub.providers.mock_provider import MockProvider

llm =  MockProvider(provider=MockProvider())

response = llm.generate("What is AI?")
print(response)