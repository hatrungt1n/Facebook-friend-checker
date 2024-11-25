# main.py
import time
from src.tracker import FriendTracker

if __name__ == "__main__":
    while True:
        FriendTracker.track()
        time.sleep(24 * 60 * 60)  # Run daily
