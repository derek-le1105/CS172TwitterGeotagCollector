# from re import A
# from matplotlib.pyplot import text
from fileinput import filename
import tweepy
import configparser
import pandas as pd
import json
import re
import os

maxFileSize = 1e+7
maxTotalFileSize = 2e+9
totalFileSizes = 0
fileCount = 0
tweetCount = 0
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

class streamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        global totalFileSizes
        global fileCount
        global tweetCount
        
        currFile = f"samplexdxd.txt"#{fileCount}.txt"
        fp = open(currFile,'a')

        file_size = os.path.getsize(currFile)
        if file_size > maxFileSize:
            fp.close()
            print(f"Closing {currFile}")
            totalFileSizes += file_size
            fileCount +=1
            if totalFileSizes > maxTotalFileSize:
                self.disconnect()
                print("2 GB reached")
        else:
            currDict = {
                'id': tweet.id,
                'text': tweet.text,
                'created_at':tweet.created_at,
                'links':self.Find(tweet.text), 
                'geo':tweet.geo
            }
            tweetCount += 1
            jsonObj = json.dumps(currDict, default=str)
            print(f'[{tweetCount}, {jsonObj}]',file=fp)
        

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
    bearer_token = config['twitter']['bearer_token']

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    streaming_client = streamListener(bearer_token)
    streaming_client.sample(tweet_fields=['id', 'text', 'author_id', 'created_at','geo'])

    