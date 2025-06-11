from serpapi import GoogleSearch
from app.core.config import settings

class SerpService:
    def __init__(self):
        self.client = GoogleSearch({
            "api_key": settings.SERPAPI_API_KEY,
            "engine": "google"
        })

    def search(self, query: str) -> list[dict]:
        params = {"q": query}
        res = self.client.get_dict(params)
        return res.get("organic_results", [])

