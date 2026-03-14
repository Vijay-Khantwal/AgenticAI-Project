class ShortTermMemory:

    def __init__(self, max_messages=3):
        self.messages = []
        self.max_messages = max_messages

    def add_message(self, role, content):

        self.messages.append({
            "type": "raw",
            "role": role,
            "content": content
        })

    def add_summary(self, text):

        self.messages.insert(0, {
            "type": "summary",
            "content": text
        })

    def get_messages(self):
        return self.messages

    def needs_summarization(self):

        raw = [m for m in self.messages if m["type"] == "raw"]

        return len(raw) > self.max_messages

    def get_old_messages(self, count=4):

        raw = [m for m in self.messages if m["type"] == "raw"]

        return raw[:count]

    def remove_old_messages(self, count=4):

        removed = 0
        new_list = []

        for m in self.messages:
            if m["type"] == "raw" and removed < count:
                removed += 1
                continue
            new_list.append(m)

        self.messages = new_list