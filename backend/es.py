from datetime import datetime
from http import client
from elasticsearch import Elasticsearch, helpers
import configparser
import os
import json

def getData():
    data = []
    for filename in os.listdir("Sample Data"):
        currFile = os.path.join("Sample Data", filename)
        print(currFile)
        if os.path.isfile(currFile):
            #print(currFile)
            with open(currFile, 'r') as file:
                for line in file:
                    #data.append(json.loads(line))
                    docSource = json.loads(line)
                    print(docSource)
                    yield {
                        "_index": "tweets",
                        "_source": docSource,
                    }

config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

client = Elasticsearch(
    cloud_id=config['elasticsearch']['cloud_id'],
    basic_auth=(config['elasticsearch']['elastic_user'], config['elasticsearch']['elastic_pw'])
)

try:
    # make the bulk call using 'actions' and get a response
    resp = helpers.bulk(
        client,
        getData()
    )
    print ("\nhelpers.bulk() RESPONSE:", resp)
    print ("RESPONSE TYPE:", type(resp))
except Exception as err:
    print("\nhelpers.bulk() ERROR:", err)