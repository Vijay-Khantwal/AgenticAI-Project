import json
import re

def parse_tool_call(llm_output):

    if "TOOL_CALL" not in llm_output:
        return None

    tool_match = re.search(r"tool:\s*(\w+)", llm_output)
    args_match = re.search(r"args:\s*(\{.*\})", llm_output)

    if not tool_match:
        return None

    tool_name = tool_match.group(1)

    args = {}
    if args_match:
        try:
            args = json.loads(args_match.group(1))
        except:
            args = {}

    return {
        "tool": tool_name,
        "args": args
    }