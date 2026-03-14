class Planner:

    def create_plan(self , user_input, context):

        return [
            {
                "action" : "llm_response",
                "input" : user_input
            }
        ]