#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response."""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('ascii'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
