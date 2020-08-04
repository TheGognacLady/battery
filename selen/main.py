from iparse import cookies
from pymongo import MongoClient
import json
import time

client = MongoClient('mongodb', 27017)
db = client.cookiebase

with open('data/accounts.json', 'r') as f:
    accounts = json.load(f)

items = db.cookies.find()

absence = accounts.keys() - set(map(lambda x: x['uname'], items))

if absence:
    for uname in absence:
        passw = accounts[uname]
        obt = cookies.CookieObtainer(uname, passw)
        cook = obt.refresh_cookies("https://www.instagram.com/")
        new = {
            'cookies': cook,
            'uname': uname,
        }
        cookies = db.cookies
        cookies.insert_one(new)

time.sleep(60)
