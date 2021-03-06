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
    cookies = db.cookies.find_one()
    uname = cookies['uname']
    db.cookies.delete_one({'uname': uname})
    return {'res': cookies['cookies']}

@app.route('/getall')
def get_db():
    cookies = db.cookies.find()
    return {'res': cookies}

if __name__ == "__main__":
    app.run(host="185.241.194.110")
