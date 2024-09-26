#!/usr/bin/python3
"""
This script fetches the status of the ALX intranet and prints the 
response body including the type, content, and utf8 content. 
It demonstrates the use of urllib to make HTTP requests in Python.
"""

import urllib.request


def fetch_status(url):
    """Fetch the status from the given URL and print the response."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
