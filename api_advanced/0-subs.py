#!/usr/bin/python3
"""Queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given,
the function should return 0.
"""
import requests

def get_subreddit_subscribers(subreddit):
   """Queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
   If an invalid subreddit is given, the function should return 0.

   Parameters:
   subreddit (str): The name of the subreddit.

   Returns:
   int: The number of subscribers in the given subreddit. If the subreddit is invalid, returns 0.
   """
   try:
       response = requests.get(f"https://api.reddit.com/r/{subreddit}/about", headers={"User-Agent": "My User Agent 1.0"})
       response.raise_for_status()
       data = response.json()
       return data["data"]["subscribers"]
   except requests.exceptions.HTTPError as e:
       if e.response.status_code == 404:
           return 0
       else:
           raise e
   except requests.exceptions.RequestException as e:
       raise e
# Testing the function with valid input
subreddit = "python"
result = get_subreddit_subscribers(subreddit)
print(result) # Should print the number of subscribers for r/python

# Testing the function with invalid input
subreddit = "invalid_subreddit"
result = get_subreddit_subscribers(subreddit)
print(result) # Should print 0