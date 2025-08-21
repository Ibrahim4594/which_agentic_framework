import openai
from .utils import format_response, save_log
from .config import Config

class OpenAIAgent:
    def __init__(self, config: Config):
        self.config = config
        openai.api_key = config.openai_api_key

    def chat(self, prompt: str, history=None) -> str:
        messages = history or []
        messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=self.config.model,
            messages=messages
        )
        result = response.choices[0].message["content"]
        save_log("chat", prompt, result)
        return format_response(result)

    def generate_code(self, instruction: str, language: str = "python") -> str:
        prompt = f"Write {language} code for the following task:\n{instruction}"
        return self.chat(prompt)

    def advanced_reasoning(self, question: str) -> str:
        prompt = f"Think step by step and answer: {question}"
        return self.chat(prompt)