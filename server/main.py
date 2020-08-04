from flask import Flask, request
from pymongo import MongoClient
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb', 27017)
db = client.cookiebase

@app.route('/generate')
def gen():
    cookies = db.cookies.find().limit(30)
    return {'res': list(map(lambda x: x['cookies'], cookies))}

if __name__ == "__main__":
    app.run(host="89.208.86.241")
