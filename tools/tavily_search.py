from tavily import TavilyClient
import os

client = TavilyClient(os.getenv("TAVILY_API_KEY"))

def tavily_search(query, advanced=False):

    depth = "advanced" if advanced else "basic"

    response = client.search(
        query=query,
        search_depth=depth,
        max_results=5
    )

    results = []

    for r in response["results"]:
        results.append({
            "title": r["title"],
            "url": r["url"],
            "content": r["content"]
        })

    return results
