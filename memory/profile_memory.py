import json
import os

class ProfileMemory:

    def __init__(self, path="storage/profile.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return {}

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_fact(self, key, value):
        self.data[key] = value
        self.save()

    def get_profile(self):
        return self.data
    
    def merge_profile(self, new_data):
        for k, v in new_data.items():

            if isinstance(v, list):

                existing = set(self.data.get(k, []))
                existing.update(v)
                
                self.data[k] = list(existing)

            else:
                self.data[k] = v

        self.save()
    