#!/usr/bin/python3
"""
Takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=HTTPBasicAuth(user, pwd))
    stuff = req.json()
    print(stuff.get('id'))
