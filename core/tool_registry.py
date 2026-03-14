from tools.tavily_search import tavily_search

TOOLS = {
    "web_search": {
        "function": tavily_search,
        "description": "Search the internet for recent information",
        "parameters": {
            "query": "string",
            "advanced" : "boolean"
        }
    }
}