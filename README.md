# AI_Top_Hub

A production-oriented multi-provider AI SDK for integrating and managing Large Language Models (LLMs) such as OpenAI and Anthropic Claude through a unified, extensible interface.

This project demonstrates scalable system design, provider abstraction, and real-world API integration, enabling developers to seamlessly switch between AI providers without changing core application logic.

---

## Key Features

- **Multi-Provider Support**: Integrates OpenAI and Anthropic Claude (extensible to more providers)
- **Unified Interface**: Standardized `generate()` method across all providers
- **Provider Abstraction Layer**: Built using Abstract Base Classes (ABC) for consistency and scalability
- **Factory Pattern Implementation**:
  - Class-based provider selection
  - Instance-based provider creation
- **Flexible Model Configuration**: Users can specify model versions dynamically
- **Environment-Based Configuration**: Secure API key handling via environment variables
- **Mock Provider Support**: Enables local testing without external API calls
- **Robust Error Handling**: Context-aware error messages for debugging and reliability

---

## System Overview

The SDK follows a modular and extensible architecture:

### 1. Provider Selection
- Dynamically selects AI provider (OpenAI, Claude, etc.)

### 2. Provider Initialization
- Allows custom configuration (model, API key, etc.)

### 3. Request Handling
- Sends prompt to selected provider API

### 4. Response Processing
- Normalizes provider-specific responses into a consistent format

### 5. Output Delivery
- Returns clean, usable text output to the user

---

## Tech Stack

- **Language**: Python 3.10+
- **AI Providers**:
  - OpenAI SDK
  - Anthropic SDK

### Core Concepts
- Object-Oriented Programming (OOP)
- Abstract Base Classes (ABC)
- Factory Design Pattern
- API Integration
- Error Handling & Validation
- Modular Software Architecture

---

## Installation

### 1. Clone the Repository
git clone https://github.com/oghenetejiritop/ai-top-hub.git  
cd ai-top-hub

### 2. Install Dependencies
pip install openai anthropic

---

## Usage Example

### Class-Based Provider Usage

```python
from ai_top_hub.core.llm import get_llm_provider

LLMClass = get_llm_provider("claude")
client = LLMClass(model="claude-sonnet-4-6")

response = client.generate("Explain AI simply")
print(response)

### Instance-Based Provider Usage

from ai_top_hub.core.llm import create_llm

llm = create_llm("openai", model="gpt-4o-mini")

response = llm.generate("What is machine learning?")
print(response)


## ai_top_hub/
• 
providers/
• 
base_provider.py # Abstract base class
• 
openai_provider.py # OpenAI implementation
• 
claude_provider.py # Claude implementation
• 
mock_provider.py # Mock provider for testing
• 
core/
• 
llm.py # Provider factory and interface logic
• 
utils/ # Configuration helpers (future use)
• 
exceptions/ # Custom exception handling (future use)
• 
README.md
• 
requirements.txt
 
### Roadmap
* Add support for additional providers (Meta AI, Grok, etc.)
* Implement configuration file support (YAML/JSON)
* Add token usage and cost tracking per provider
* Introduce fallback provider mechanism
* Build CLI interface for quick interaction
* Add unit and integration testing
* Package and publish to PyPI
 
### Example Output

Explain AI simply:

AI is a technology that allows machines to learn from data and make decisions...
 
  ## Author
 
Oghenetejiri Peace Onosajerhe
- [GitHub](https://github.com/oghenetejiritop)
- [LinkedIn](https://linkedin.com/in/oghenetejiritop) 

 ## License

 This project is licensed under the MIT License.