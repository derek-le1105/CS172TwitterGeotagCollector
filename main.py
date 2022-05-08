import tweepy
import configparser

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
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    place = api.search_geo(query="india", granularity="country")
    #print(place[0].id)

    new_tweets = []
    new_tweets = api.search_tweets(q='place:%s' % place[0].id, count=100)
    
    print(new_tweets[0])