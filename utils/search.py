from tavily import TavilyClient
from config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)


def web_search(query):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )

    return response