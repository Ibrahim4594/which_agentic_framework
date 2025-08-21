class Config:
    def __init__(self, openai_api_key: str, model: str = "gpt-4o"):
        self.openai_api_key = openai_api_key
        self.model = model

    def load_from_file(self, file_path):
        import json
        with open(file_path, 'r') as f:
            config_data = json.load(f)
            self.api_key = config_data.get('api_key')
            self.model = config_data.get('model')

    def validate(self):
        if not self.api_key:
            raise ValueError("API key is required.")
        if not self.model:
            raise ValueError("Model is required.")