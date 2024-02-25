"""
Script to send a request to a URL and display the value of the X-Request-Id header.
"""

import requests
import sys

def get_x_request_id(url):
    """
    Sends a request to the given URL and returns the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request.

    Returns:
        str: The value of the X-Request-Id header.

    Raises:
        requests.exceptions.RequestException: If the request encounters an error.
    """
    response = requests.get(url)
    return response.headers.get('X-Request-Id')

if __name__ == "__main__":
    # Check if a URL is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Fetching the X-Request-Id header value
    x_request_id = get_x_request_id(url)

    # Displaying the X-Request-Id header value
    print(x_request_id)