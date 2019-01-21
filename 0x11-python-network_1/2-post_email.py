#!/usr/bin/python3
"""
Takes in a URL and email, sends a POST request to the
URL with the email as a parameter, and displays the body
of the response
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    data = parse.urlencode(email).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read()
    print(html.decode())
