"""
Script to send a POST request with an email parameter to a given URL.
"""

import requests
import sys

def post_email(url, email):
    """
    Sends a POST request with the email as a parameter to the given URL.

    Args:
        url (str): The URL to send the POST request.
        email (str): The email address to include in the request.

    Returns:
        requests.models.Response: The response object.

    Raises:
        requests.exceptions.RequestException: If the request encounters an error.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response

if __name__ == "__main__":
    # Check if both URL and email are provided as command line arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Sending POST request with email parameter
    response = post_email(url, email)

    # Displaying the body of the response
    print(response.text.strip())