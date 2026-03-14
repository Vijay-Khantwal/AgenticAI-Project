# load environment variables
from dotenv import load_dotenv
load_dotenv()

import os
from core.agent import Agent

agent = Agent()

while True:
    print("You (finish with empty line):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    user = "\n".join(lines)

    if user.strip() == "exit":
        break

    response = agent.chat(user)

    print("Agent:", response)