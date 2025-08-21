import pytest
from openai_agent.agent import OpenAIAgent

@pytest.fixture
def agent():
    return OpenAIAgent()

def test_initialize(agent):
    assert agent.initialize() is True

def test_run(agent):
    input_data = "Hello, how can I help you?"
    response = agent.run(input_data)
    assert response is not None
    assert isinstance(response, str)

def test_shutdown(agent):
    assert agent.shutdown() is True