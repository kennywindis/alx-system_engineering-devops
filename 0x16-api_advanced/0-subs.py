#!/usr/bin/python3
# -*- coding: utf-8 -*-

from json import loads
from requests import get


def number_of_subscribers(subreddit):
    """ecursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent':
        'My User Agent 1.0'
    }
    response = get(url, headers=headers)
    reddits = response.json()

    try:
        subscribers = reddits.get('data').get('subscribers')
        return int(subscribers)
    except:
        return 0
