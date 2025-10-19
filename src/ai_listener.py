import requests
import json

class AiListener:

    def __init__(self):
        # Fallback to self-hosted ollama server.
        self.url = "http://localhost:11434/api/chat"
        self.model = "gemma3"

    def request(self, message):
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": message}]
        }

        response = requests.post(self.url, json=payload, stream=True)
        
        if response.status_code == 200:
            for line in response.iter_lines(True):
                json_data = json.loads(line)
                print(json_data["message"]["content"], end="", flush=True)
        print()
