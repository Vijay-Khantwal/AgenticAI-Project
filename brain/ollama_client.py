import requests

class OllamaClient:
    
    def generate(self , prompt):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5-coder:7b",
                "prompt": prompt,
                "stream": False
            }

        )
        return response.json()["response"]