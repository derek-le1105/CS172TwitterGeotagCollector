# from re import A
# from matplotlib.pyplot import text
import tweepy
import configparser
import pandas as pd
import json

maxFileSize = 1e+7

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
    queryList = ['Orange County', 'Los Angeles', 'Riverside', 'dog', 'nba', 'met gala', 'johnny depp', 'amber heard']
    #print("The text of the status is : \n\n" + text)
    
    # The method returns a Response object, a named tuple with data, includes,
    # errors, and meta fields
    #print(response.meta)

    # In this case, the data field of the Response returned is a list of Tweet
    # objects

    test = []
    # Each Tweet object has default ID and text fields

    for query in queryList:
        #print(query)
        response = client.search_recent_tweets(query=query, tweet_fields=['geo', 'created_at', 'author_id'], max_results=100)    
        tweets = response.data
        for tweet in tweets:
            #temp = api.get_status(tweet.id)
            if tweet.geo != None:# or temp.place != None:
               json_object = json.dumps(tweet.data)
               print(json_object)
               test.append(json_object)
        
    with open("sample.txt", "w") as outfile:
        for i in test:
            outfile.write(i + '\n')
        print(outfile.tell())
    # By default, this endpoint/method returns 10 results
    # You can retrieve up to 100 Tweets by specifying max_results
    #print(test)
    