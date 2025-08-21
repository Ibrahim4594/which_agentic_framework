# OpenAI Agent SDK

## Overview
The OpenAI Agent SDK is a Python library designed to facilitate the integration and interaction with OpenAI's API. It provides a structured way to create and manage agents that can process inputs, generate responses, and handle various tasks using OpenAI's capabilities.

## Features
- Easy-to-use interface for creating OpenAI agents.
- Core logic for processing inputs and generating responses.
- Configuration management for API keys and model settings.
- Utility functions for logging and response formatting.
- Comprehensive unit tests to ensure reliability.

## Installation
To install the OpenAI Agent SDK, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd openai_agent_sdk
pip install -r requirements.txt
```

## Usage
Here's a simple example of how to use the OpenAI Agent SDK:

```python
from openai_agent.agent import OpenAIAgent

agent = OpenAIAgent()
agent.initialize()
response = agent.run("Hello, how can I assist you today?")
print(response)
agent.shutdown()
```

## Configuration
To configure the SDK, you can set your API key and model in a configuration file or directly in your code:

```python
from openai_agent.config import Config

config = Config()
config.load_from_file('config.json')
```

## Running Tests
To run the unit tests for the SDK, use the following command:

```bash
pytest src/tests
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
