from re import A
from matplotlib.pyplot import text
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

    client = tweepy.Client(bearer_token=bearer_token)
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
  
    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)
    
    # calling the api 
    api = tweepy.API(auth)
    tweet_ids = [1460323737035677698, 1293593516040269825, 1293595870563381249]
    id = 1272771459249844224
    
    # fetching the status
    #status = api.get_status(id)
    
    # fetching the text attribute
    #text = status.text 
    
    #print("The text of the status is : \n\n" + text)
    for ids in tweet_ids:
        status = api.get_status(ids)
        text = status.text
        print(text)
    