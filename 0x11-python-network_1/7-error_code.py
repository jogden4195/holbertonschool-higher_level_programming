#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and
displays the body fo the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except:
        print("Error code: {}".format(r.status_code))
