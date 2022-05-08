# from re import A
# from matplotlib.pyplot import text
import tweepy
import configparser
import pandas as pd
import json

class streamListener(tweepy.StreamingClient):
    # def on_tweet(self, tweet):
    #     print(tweet.id)
    #     #return super().on_tweet(tweet)
    def on_data(self, data):
        print(data)
        #return super().on_includes(includes)

config = configparser.ConfigParser()
config.read('config.ini')

bearer_token = "AAAAAAAAAAAAAAAAAAAAAHnicAEAAAAANDnnmfkWKi6JI0bPplQs%2B35dj8o%3DxdfVtJx7kfob9G3N4aYjmLR7DWlpXGiShWqxcsY4HsckOBMZMi"

if __name__ == "__main__":
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    client = tweepy.Client(bearer_token=bearer_token)
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
  
    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)

    streaming_client = streamListener(bearer_token)
    streaming_client.add_rules(tweepy.StreamRule('has:geo'))
    streaming_client.filter()

    