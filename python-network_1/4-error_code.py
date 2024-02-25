"""
Script to send a request to a URL and display the body of the response.
Prints an error message if the HTTP status code is greater than or equal to 400.
"""

import requests
import sys

def display_response(url):
    """
    Sends a request to the given URL and displays the body of the response.
    Prints an error message if the HTTP status code is greater than or equal to 400.

    Args:
        url (str): The URL to send the request.

    Returns:
        None
    """
    response = requests.get(url)
    print(response.text)

    # Check if HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

if __name__ == "__main__":
    # Check if a URL is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: ./4-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Displaying the response and handling errors
    display_response(url)