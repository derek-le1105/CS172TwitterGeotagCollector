import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

bearer_token = "AAAAAAAAAAAAAAAAAAAAAHnicAEAAAAANDnnmfkWKi6JI0bPplQs%2B35dj8o%3DxdfVtJx7kfob9G3N4aYjmLR7DWlpXGiShWqxcsY4HsckOBMZMi"

if __name__ == "__main__":
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']
    #bearer_token = config['twitter']['bearer_token']

    # auth = tweepy.OAuthHandler(api_key, api_key_secret)
    # auth.set_access_token(access_token, access_token)

    # api = tweepy.API(auth)

    # public_tweets = api.get_followers()
    # print(public_tweets)
    # client = tweepy.Client(
    #     consumer_key=api_key,
    #     consumer_secret=api_key_secret,
    #     access_token=access_token, 
    #     access_token_secret=access_token_secret
    # )
    client = tweepy.Client(bearer_token=bearer_token)

    response = client.search_recent_tweets(
    "Tweepy", tweet_fields=["created_at", "lang"]
    )
    tweets = response.data

    # You can then access those fields as attributes of the Tweet objects
    for tweet in tweets:
        print(tweet.id, tweet.lang)

    # Alternatively, you can also access fields as keys, like a dictionary
    for tweet in tweets:
        print(tweet["id"], tweet["lang"])

    # There’s also a data attribute/key that provides the entire data dictionary
    for tweet in tweets:
        print(tweet.data)
    