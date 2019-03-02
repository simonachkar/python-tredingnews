""" Get top trending topics on twitter in real-time """

import tweepy

# API Keys and Tokens
consumer_key = '7KoC7msyJdL5klqmPV3sDadtW'
consumer_secret = 'tbwPerllnKwlokw1b2EGe6KWEHRcS3e0zF61pYELBDQ6wioFVT'
access_token = '1040179359628386306-EKw17SgDpAi0wPknTvYPQza8vfiGbm'
access_token_secret = 'FzTL7te7MV5N6jY2ywsP9j62JD7KKtvNYG1F5DTLwsJ5H'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Trending topics in toronto (WOEID of Toronto = 4118)
trending_topics = api.trends_place(1, exclude="hashtags")


def get_twitter_trends():
    trends_list = []
    for trends in trending_topics:
        for trend in trends["trends"]:
            trends_list.append(trend["name"])
    return trends_list
