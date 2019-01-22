#!/usr/bin/python3
"""
Takes in a string and sends a search request to
the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/?search=' + argv[1]
    req = requests.get(url)
    stuff = req.json()
    if stuff:
        print("Number of results: {}".format(stuff.get("count")))
        for result in stuff.get("results"):
            print(result.get("name"))
