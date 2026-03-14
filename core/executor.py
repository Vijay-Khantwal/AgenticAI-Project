from brain.llm_interface import LLMInterface
llm = LLMInterface()
class Executor:

    def execute(self, plan):

        results = []

        for step in plan:

            if step["action"] == "llm_response":
                results.append(llm.generate(step["input"]))

        return results