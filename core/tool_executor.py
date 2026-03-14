from core.tool_registry import TOOLS


class ToolExecutor:

    def execute(self, tool_name, args):

        if tool_name not in TOOLS:
            return f"Tool {tool_name} not found"

        tool = TOOLS[tool_name]["function"]

        try:
            result = tool(**args)
            return result
        except Exception as e:
            return f"Tool execution failed: {str(e)}"
