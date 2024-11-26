# src/tracker.py
from fetcher import FriendFetcher
from storage import FriendStorage
from logger import EventLogger
from notifier import Notifier

class FriendTracker:
    """Tracks and handles unfriending events."""

    @staticmethod
    def track():
        old_friends = FriendStorage.load_friend_list()
        current_friends = FriendFetcher.fetch_friend_list()

        unfriended = set(old_friends) - set(current_friends)

        for friend in unfriended:
            Notifier.notify(friend)
            EventLogger.log_event(friend)

        FriendStorage.save_friend_list(current_friends)
