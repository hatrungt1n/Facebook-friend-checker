# src/notifier.py
class Notifier:
    """Handles notifications for unfriending events."""

    @staticmethod
    def notify(friend):
        print(f"❌ {friend} unfriended you!")
