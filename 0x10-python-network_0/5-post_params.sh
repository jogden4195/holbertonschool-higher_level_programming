#!/bin/bash
#Takes in an URL, sends a POST request, and displays the body of the response
curl -sl --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
