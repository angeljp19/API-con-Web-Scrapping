from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util

client = MongoClient('localhost', 27017)
db = client.currencyPair


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/price')
def price():
    symbol = request.args.get('symbol')
    collection = db[symbol]
    data = collection.find().sort("_id", -1).limit(1)
    return json.loads(json_util.dumps(data))


if __name__ =="__main__":
    app.run()

