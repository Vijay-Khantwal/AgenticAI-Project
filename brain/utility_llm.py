from brain.gemma_client import GemmaClient

llm = GemmaClient()

class UtilityLLM:

    def summarize(self, text):

        prompt = f"""
Summarize the following conversation in 1-2 sentences.
Keep important context.

Conversation:
{text}
"""

        return llm.supportGen(prompt)

    def extract_profile(self, message , current_profile):

        prompt = f"""
You are a system that updates a user's permanent profile memory.

Current user profile:
{current_profile}

New message from the user:
{message}

Extract any NEW permanent information about the user and update the profile.

Rules:
- Only include NEW information found in the message
- Do not repeat existing information
- Do not remove existing profile data
- Avoid duplicates
- If nothing new is found, return an empty JSON object: {{}}
- The response MUST be valid JSON
- Do NOT include explanations
- Do NOT include markdown
- Do NOT include ```json
- Return ONLY raw JSON

Example outputs:
{{"interests": ["anime"]}}
{{"name": "Vikash"}}
{{}}
"""

        response = llm.supportGen(prompt)
        return response