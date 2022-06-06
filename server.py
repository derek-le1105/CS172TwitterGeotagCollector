import json
import configparser
from time import sleep
from datetime import datetime
from elasticsearch import Elasticsearch, helpers
from flask import Flask, request
from flask_cors import CORS

def sampleDataToStr(self):
    strList = []
    for line in open(str(self), encoding="utf8", errors='ignore'):
        strList.append(line)
    return strList
    
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

client = Elasticsearch(
    cloud_id=config['elasticsearch']['cloud_id'],
    basic_auth=(config['elasticsearch']['elastic_user'], config['elasticsearch']['elastic_pw'])
)

app = Flask(__name__)
CORS(app)

tweetDocs = sampleDataToStr("Sample Data/sample0.txt")

docList = []    #empty list for elasticsearch docs

for count, doc in enumerate(tweetDocs):
    try:
        dict_doc = json.loads(doc)
        dict_doc["timestamp"] = datetime.now()
        dict_doc["_id"] = count

        docList += [dict_doc]

    except json.decoder.JSONDecodeError as err:
        print(f"error at num {count} | JSONDecodeError {err} | doc: {doc}")

try:
    resp = helpers.bulk(   #use helpers.bulk API to index elasticsearch docs
        client,
        docList,
        index = "tweets"
    )

    print ("bulk API resp:", resp, json.dumps(resp, indent=4))
except Exception as err:
    print("bulk() err: ", err)
    quit()

# These are the endpoints
@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route("/getData", methods=['POST'])
def getData():
    print(request.json) # This is the input
    input = request.json['dataToFetch']
    print(input) 
    
    query_search = {
        'query': {
            "query_string" : {
                "query" : input
            }
        }
    }

    resp = client.search(
        index = "tweets",
        body = query_search
    )

    print ("search():", json.dumps(resp.body, indent=4))
    return json.dumps(resp.body, indent=4)