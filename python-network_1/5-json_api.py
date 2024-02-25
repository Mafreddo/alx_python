"""
Script to send a POST request with a letter parameter to http://0.0.0.0:5000/search_user.
Displays the id and name from the JSON response or an error message.
"""

import requests
import sys

def search_user(letter):
    """
    Sends a POST request with the given letter as a parameter to http://0.0.0.0:5000/search_user.

    Args:
        letter (str): The letter to include in the request.

    Returns:
        requests.models.Response: The response object.

    Raises:
        requests.exceptions.RequestException: If the request encounters an error.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    return response

def display_user_info(response):
    """
    Displays the id and name from the JSON response or an error message.

    Args:
        response (requests.models.Response): The response object.
    """
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    # Check if a letter is provided as a command line argument
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    # Sending POST request with letter parameter
    response = search_user(letter)

    # Displaying user information or an error message
    display_user_info(response)