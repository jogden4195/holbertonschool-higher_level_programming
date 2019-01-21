#!/usr/bin/python3
"""
Prints the X-Request-Id value of the given url
"""
import urllib.request
import sys


url = sys.argv[1]
res = urllib.request.urlopen(url)
with res as response:
    html = dict(response.info())
print(html.get('X-Request-Id'))
