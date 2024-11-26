# Facebook Friend Tracker

## Description
A Python-based tool designed to track changes in a user's Facebook friend list, such as when someone unfriends the user. This project uses the Facebook Graph API to retrieve friend data and logs any changes in the friend list over time.

## Purpose
The purpose of this project is to help users monitor their Facebook friend list to detect when someone unfriends them. It also serves as a practical example of working with the Facebook Graph API in a Python application.

## Why This Tool Cannot Run Currently
Due to Facebook's privacy restrictions introduced in 2018, the Graph API endpoint `/me/friends` only returns friends who are mutual users of the app. This means:
1. You will only see friends who have also logged into the app and granted the `user_friends` permission.
2. The API does not provide access to a full list of Facebook friends anymore.
3. Additionally, Facebook has temporarily disabled the creation of test users, making it harder to test this app. https://developers.facebook.com/docs/development/build-and-test/test-users/

These limitations are imposed by Facebook and cannot be bypassed yet.

## How to Run

### Prerequisites
1. **Python 3.8 or later**: Ensure Python is installed on your system.
2. **Facebook Developer Account**: You need access to the [Facebook Developer Portal](https://developers.facebook.com/) to create an app and generate an access token.
3. **Required Permissions**: Your app must have the `user_friends` permission enabled. However, this requires Facebook's App Review process.

### Setup Instructions
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/facebook-friend-tracker.git
   cd facebook-friend-tracker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create and fill data in a .env file

4. Run the tool:
   ```bash
   python src/main.py
   ```