#!/usr/bin/python3
"""Queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If not a valid subreddit, returns 0.
    """
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    response = requests.get(url, headers=headers)
    
    # If the response status code is 404, the subreddit is not valid
    if response.status_code == 404:
        return 0
    
    # If the response status code is 200, the subreddit is valid
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    
    # If the response status code is neither 404 nor 200, there was an error
    raise Exception(f'Error {response.status_code}: {response.text}')