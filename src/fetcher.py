# src/fetcher.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
GRAPH_API_URL = os.getenv("GRAPH_API_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

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
            print("data: ", data)
            if "error" in data:
                raise Exception(f"API Error: {data['error']['message']}")
            
            return [friend["name"] for friend in data.get("data", [])]
        except Exception as e:
            print(f"Error fetching friend list: {e}")
            return []
