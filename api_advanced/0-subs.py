#!/usr/bin/python3
"""
reddit_subscribers.py

This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit. It handles invalid subreddit names by
returning 0 and ensures that redirects to search results are not followed.

Features:
- Returns subscriber count for an existing subreddit.
- Returns 0 for a nonexisting or invalid subreddit.
- Uses a custom User-Agent to avoid request errors.
- Follows PEP8 guidelines for formatting and style.

Example usage:
    python_subs = number_of_subscribers("python")
    print(f"Python subreddit subscribers: {python_subs}")

    fake_subs = number_of_subscribers("thissubdoesnotexist123")
    print(f"Nonexisting subreddit subscribers: {fake_subs}")
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/58.0.3029.110 Safari/537.3'
        )
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0


if __name__ == "__main__":
    # Output: existing subreddit
    print("Python subreddit subscribers:", number_of_subscribers("python"))

    # Output: nonexisting subreddit
    print("Nonexisting subreddit subscribers:",
