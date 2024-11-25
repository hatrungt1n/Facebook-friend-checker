# src/storage.py
import json
from src.config import FRIENDS_FILE

class FriendStorage:
    """Handles saving and loading the friend list."""

    @staticmethod
    def load_friend_list():
        try:
            with open(FRIENDS_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_friend_list(friends):
        with open(FRIENDS_FILE, "w") as file:
            json.dump(friends, file)
