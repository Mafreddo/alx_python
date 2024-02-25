"""
Script to use the GitHub API to display the user id.
Uses Basic Authentication with a personal access token.
"""

import requests
import sys

def get_github_user_id(username, password):
    """
    Uses the GitHub API to get the user id.

    Args:
        username (str): GitHub username.
        password (str): Personal access token as the password.

    Returns:
        int: The user id if successful, None otherwise.

    Raises:
        requests.exceptions.RequestException: If the request encounters an error.
    """
    url = "https://api.github.com/user"
    auth = (username, password)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        return response.json().get('id')
    else:
        return None

if __name__ == "__main__":
    # Check if both username and password are provided as command line arguments
    if len(sys.argv) != 3:
        print("Usage: ./6-my_github.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    # Getting GitHub user id
    user_id = get_github_user_id(username, password)

    # Displaying the user id or None if the authentication fails
    print(user_id)