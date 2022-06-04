from datetime import datetime
from elasticsearch import Elasticsearch
import configparser
import os

def getData(file):
    data = []

    for line in open(file):
        data += 

config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

es = Elasticsearch(
    cloud_id=config['elasticsearch']['cloud_id'],
    basic_auth=(config['elasticsearch']['elastic_user'], config['elasticsearch']['elastic_pw'])
)

for filename in os.listdir("Sample Data"):
    currFile = os.path.join("Sample Data", filename)
    if os.path.isfile(currFile):
        #print(currFile)
        with open(currFile, 'r') as file:
            line = file.read()