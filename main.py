# from re import A
# from matplotlib.pyplot import text
import tweepy
import configparser
import pandas as pd
import json
import re
import os

maxFileSize = 1e+7
config = configparser.ConfigParser()
config.read('config.ini')
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHnicAEAAAAANDnnmfkWKi6JI0bPplQs%2B35dj8o%3DxdfVtJx7kfob9G3N4aYjmLR7DWlpXGiShWqxcsY4HsckOBMZMi"

class streamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        currDict = {
            'id': tweet.id,
            'text': tweet.text,
            'created_at':tweet.created_at,
            'links':self.Find(tweet.text),
            'geo':tweet.geo
        }
        jsonObj = json.dumps(currDict, default=str)
        fp = open('sample.txt','a')
        print(jsonObj,file=fp)
        file_size = os.path.getsize('sample.txt')
        if file_size > maxFileSize:
            fp.close()
            self.disconnect()

    def Find(self, string):    #retrieved from https://www.geeksforgeeks.org/python-check-url-string/
        # findall() has been used 
        # with valid conditions for urls in string
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)      
        return [x[0] for x in url]

if __name__ == "__main__":
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    client = tweepy.Client(bearer_token=bearer_token)
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
  
    # set access to user's access key and access secretz 
    auth.set_access_token(access_token, access_token_secret)

    streaming_client = streamListener(bearer_token)
    #streaming_client.add_rules(tweepy.StreamRule('python lang:en -has:media -is:retweet'))
    streaming_client.sample(tweet_fields=['id', 'text', 'author_id', 'created_at','geo'])
    #streaming_client.sample(tweepy.StreamRule('-has:media'), tweet_fields=['id', 'text', 'author_id', 'created_at','geo'])

    