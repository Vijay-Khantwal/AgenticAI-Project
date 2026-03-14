from openai import OpenAI
import os

class PhiClient:

    def __init__(self):
        api_key = os.getenv("PHI_API_KEY")

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )

        self.model = "microsoft/phi-3.5-mini-instruct"

    def generate(self, prompt):

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                top_p=0.7,
                max_tokens=512,
                stream=False
            )

            if completion.choices:
                message = completion.choices[0].message
                if message and message.content:
                    return message.content.strip()

            return "No response from Phi."

        except Exception as e:
            return f"Phi API Error: {e}"

    def supportGen(self, prompt):
        return self.generate(prompt)