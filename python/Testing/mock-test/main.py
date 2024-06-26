import requests
import unittest
from unittest.mock import patch

def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    url = "http://api.icnbd.com/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['value']['joke']
    else:
        joke = 'No jokes'

    return joke

if __name__ == '__main__':
    print(get_joke())