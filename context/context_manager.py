from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d")

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

class ContextManager:

    def __init__(self, memory_manager):
        self.memory = memory_manager

    def build_prompt(self, user_input):

        profile = self.memory.profile.get_profile()
        summary = self.memory.summary.load()
        messages = self.memory.short_term.get_messages()

        prompt = f"SYSTEM: You are an intelligent AI assistant with access to external tools.\nCurrent date: {current_date}\n\n"

        prompt += """You may use tools if the user's request requires external information.

Available tools:

web_search(query)
- Searches the internet for recent or unknown information.
Use advanced=true only for deep research queries.
For normal information lookup use default search.


When you decide to use a tool, respond ONLY in this exact format:

TOOL_CALL
tool: web_search
args: {"query":"search query" , "advanced" : boolean}

If a tool is NOT required, respond in this format:

FINAL_ANSWER
<your response to the user>

Do not include explanations outside these formats.
\n
"""

        if profile:

            prompt += "USER PROFILE\n"

            for k, v in profile.items():
                prompt += f"{k}: {v}\n"

            prompt += "\n"

        if summary:

            prompt += "GLOBAL SUMMARY\n"
            prompt += summary + "\n\n"

        prompt += "CONVERSATION\n"

        for m in messages:

            if m["type"] == "summary":
                prompt += f"[Summary] {m['content']}\n"

            else:
                prompt += f"{m['role']}: {m['content']}\n"

        prompt += f"\nuser: {user_input}\nassistant:"

        print(f"{Colors.GREEN}{prompt}{Colors.RESET}")

        return prompt
    
