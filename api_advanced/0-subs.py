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

def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a given subreddit.
    """
    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Get the Response of the Reddit API
    res = requests.get(api_uri, headers=user_agent,
                       allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code in [302, 404]:
        return 0

    # Returns the total subscribers of the subreddit
    return res.json().get('data').get('subscribers')
