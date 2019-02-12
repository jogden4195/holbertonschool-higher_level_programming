# 0x11. Python - Network #1
## Description
At the end of this project, you expected to be able to explain to anyone, *without the help of Google*:
* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests`
* How to make HTTP `GET` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## Files
| File Name | Task Name | Description |
| --------- | --------- | ----------- |
| 0-hbtn_status.py | What's my status \#0 | Fetches `https://intranet.hbtn.io/status` |
| 1-hbtn_header.py | Response header value \#0 | Takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response |
| 2-post_email.py | POST an email \#0 | Takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`) |
| 3-error_code.py | Error code \#0 | Takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8` |
| 4-hbtn_status.py | What's my status \#1 | Fetches `https://intranet.hbtn.io/status` (using `requests`) |
| 5-hbtn_header.py | Response header valuse \#1 | Takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header (Using `requests`) |
| 6-post_email.py | POST an email \#1 | Takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response |
| 7-error_code.py | Error code \#1 | Takes in a URL, sends a request to the URL and displays the body of the response |
| 8-json_api.py | Search API | Takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter |
| 9-starwars.py | Star Wars API \#0 | Takes in a string and sends a search request to the Star Wars API |
| 10-my_github.py | My Github! | Takes your Github credentials (username and password) and uses the Github API to display your `id` |

## Author
Jenn Ogden
