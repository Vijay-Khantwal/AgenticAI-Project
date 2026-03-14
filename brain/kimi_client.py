from openai import OpenAI
import os


class KimiClient:

    def __init__(self):
        api_key = os.getenv("KIMI_API_KEY")

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )

        self.model = "moonshotai/kimi-k2-instruct"

    def generate(self, prompt):

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            top_p=0.9,
            max_tokens=4096,
            stream=False
        )

        return completion.choices[0].message.content

    def supportGen(self, prompt):

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            top_p=0.9,
            max_tokens=4096,
            stream=False
        )

        return completion.choices[0].message.content