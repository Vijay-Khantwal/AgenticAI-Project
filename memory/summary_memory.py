import os

class SummaryMemory:

    def __init__(self, path="storage/chat_summary.txt"):
        self.path = path

    def load(self):

        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return f.read()

        return ""

    def update(self, new_summary):

        old = self.load()

        combined = old + "\n" + new_summary

        with open(self.path, "w") as f:
            f.write(combined)