#!/usr/bin/python3
"""
This script fetches the status of the ALX intranet and prints the
response body including the type, content, and utf8 content.
It demonstrates the use of urllib to make HTTP requests in Python.
"""
if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
