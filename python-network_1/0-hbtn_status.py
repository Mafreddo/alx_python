"""
Script to fetch and display the status of a URL using the requests package.

Usage:
    ./0-hbtn_status.py | cat -e
"""

import requests

def get_url_status(url):
    """
    Fetches the status of the given URL using the requests package.

    Args:
        url (str): The URL to fetch.

    Returns:
        requests.models.Response: The response object.

    Raises:
        requests.exceptions.RequestException: If the request encounters an error.
    """
    response = requests.get(url)
    return response

def display_response_info(response):
    """
    Displays information about the response in the specified format.

    Args:
        response (requests.models.Response): The response object.
    """
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    # URL to fetch
    url = "https://alu-intranet.hbtn.io/status"

    # Fetching the URL status
    response = get_url_status(url)

    # Displaying information about the response
    display_response_info(response)