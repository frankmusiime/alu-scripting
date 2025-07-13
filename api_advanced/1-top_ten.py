#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """Prints the top ten hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        json_data = response.json()
        data = json_data.get("data")
        if data is None:
            print(None)
            return
        
        children = data.get("children", [])
        if len(children) == 0:
            print(None)
            return
        
        for child in children:
            child_data = child.get("data")
            if child_data:
                title = child_data.get("title")
                if title:
                    print(title)
    except (ValueError, KeyError, TypeError):
        print(None)
