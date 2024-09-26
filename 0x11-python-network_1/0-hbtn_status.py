#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    # Fetching the URL
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        # Displaying the response
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")

