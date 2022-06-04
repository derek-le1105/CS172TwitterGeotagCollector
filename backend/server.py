from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route("/getData", methods=['POST'])
def getData():
    print(request.json)
    return {"data": "some sort of data"}