# src/fetcher.py
import requests
from src.config import ACCESS_TOKEN, GRAPH_API_URL

class FriendFetcher:
    """Handles fetching friend list from Facebook Graph API."""
    
    @staticmethod
    def fetch_friend_list():
        try:
            response = requests.get(
                GRAPH_API_URL,
                params={"access_token": ACCESS_TOKEN}
            )
            data = response.json()
            if "error" in data:
                raise Exception(f"API Error: {data['error']['message']}")
            
            return [friend["name"] for friend in data.get("data", [])]
        except Exception as e:
            print(f"Error fetching friend list: {e}")
            return []
