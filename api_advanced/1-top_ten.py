#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit
        
    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return
            
        json_data = response.json()
        if not json_data or 'data' not in json_data:
            print(None)
            return
            
        data = json_data['data']
        children = data.get('children', [])
        
        if not children:
            print(None)
            return
            
        # Print titles of first 10 posts
        for post in children[:10]:
            post_data = post.get('data', {})
            title = post_data.get('title', '')
            if title:
                print(title)
            
    except (requests.RequestException, ValueError, KeyError):
        print(None)
