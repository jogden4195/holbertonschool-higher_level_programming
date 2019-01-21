#!/usr/bin/python3
"""
Fetches the url https://intranet.hbtn.io/status
"""
import urllib.request

res = urllib.request.urlopen('https://intranet.hbtn.io/status')
with res as response:
    html = response.read()
    charset = response.info().get_content_charset()
print('Body response:')
print('\t- type: {}'.format(type(html)))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode("utf-8")))
