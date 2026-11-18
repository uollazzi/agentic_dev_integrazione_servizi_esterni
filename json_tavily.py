from tavily import TavilyClient
import os
import json
from models.tavily_models import TavilySearchResponse


def search(q: str):
    api_key = os.environ.get("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY non trovata")

    tavily_client = TavilyClient(api_key=api_key)

    response = tavily_client.search(q)

    with open("logs/tavily.json", "w", encoding="utf8") as f:
        f.write(json.dumps(response, indent=2))

    return TavilySearchResponse.model_validate(response)
