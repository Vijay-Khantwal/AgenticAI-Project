from memory.memory_manager import MemoryManager
from context.context_manager import ContextManager
from brain.llm_interface import LLMInterface
from core.tool_parser import parse_tool_call
from core.tool_executor import ToolExecutor

llm = LLMInterface()

class Agent:

    def __init__(self):

        self.memory = MemoryManager()
        self.context = ContextManager(self.memory)
        self.tool_executor = ToolExecutor()


    def chat(self, user_input):


        prompt = self.context.build_prompt(user_input)
        messages = [
            {"role": "user", "content": user_input}
        ]

        llm_response = llm.generate(prompt)
        tool_call = parse_tool_call(llm_response)
        print(llm_response)

        if tool_call:

            tool_result = self.tool_executor.execute(
                tool_call["tool"],
                tool_call["args"]
            )
            print("Tool result: ", tool_result)

            tool_prompt = prompt + "\n\nTOOL RESULT:\n" + str(tool_result) + "\n\nassistant:"

            final_answer = llm.generate(tool_prompt)

            self.memory.process_user_message(user_input)
            self.memory.process_assistant_message(llm_response)

            return final_answer

    
        self.memory.process_user_message(user_input)
        self.memory.process_assistant_message(llm_response)
        return llm_response

        # return response
    
