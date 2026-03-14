from google import genai
import os


class GemmaClient:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key = api_key)

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model="gemma-3-27b-it",
            contents=prompt
        )

        return response.text
    
    def supportGen(self, prompt):

        response = self.client.models.generate_content(
            model="gemma-3-27b-it",
            contents=prompt
        )
        return response.text