from iparse import cookies
from pymongo import MongoClient
import json
import time

client = MongoClient('mongodb', 27017)
db = client.cookiebase

items = db.cookies.find()
print(items)

with open('data/accounts.json', 'r') as f:
    accounts = json.load(f)
    print(accounts)

while True:
    absence = set(accounts.keys()) - set(map(lambda x: x['uname'], items))


    if absence:
        for uname in absence:
            obt = cookies.CookieObtainer()
            passw = accounts[uname]
            cookies = obt.get_cookies(uname, passw)
            db.cookies.insert_one({
                'cookies': cookies,
                'uname': uname,
    		})

    time.sleep(1)
