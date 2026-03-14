from .short_term import ShortTermMemory
from .profile_memory import ProfileMemory
from .summary_memory import SummaryMemory
import json
from brain.utility_llm import UtilityLLM

class MemoryManager:

    def __init__(self):
        self.short_term = ShortTermMemory()
        self.profile = ProfileMemory()
        self.summary = SummaryMemory()
        
        self.utility_llm = UtilityLLM()

    def add_user_message(self, text):
        self.short_term.add_message("user", text)

    def add_assistant_message(self, text):
        self.short_term.add_message("assistant", text)

    def get_recent_chat(self):
        return self.short_term.get_messages()

    def get_profile(self):
        return self.profile.get_profile()

    def get_summary(self):
        return self.summary.load()

    def process_user_message(self, text):

        self.short_term.add_message("user", text)

        self.extract_profile_memory(text)

        if self.short_term.needs_summarization():
            self.compress_memory()

    def process_assistant_message(self, text):

        self.short_term.add_message("assistant", text)

    def extract_profile_memory(self, text):

        keywords = ["i am", "my name", "i like","i also like", "i prefer", "i work"]

        if not any(k in text.lower() for k in keywords):
            return
        print("sent for profile extraction")
        
        profile = self.profile.get_profile()

        response = self.utility_llm.extract_profile(text , profile)

        print("pro  " + response)

        try:
            data = json.loads(response)
            self.profile.merge_profile(data)

        except:
            pass

    def compress_memory(self):

        old_messages = self.short_term.get_old_messages()

        convo = "\n".join([
            f"{m['role']}: {m['content']}"
            for m in old_messages
        ])

        summary = self.utility_llm.summarize(convo)

        self.short_term.remove_old_messages()

        self.short_term.add_summary(summary)

        self.summary.update(summary)