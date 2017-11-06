from pymongo import MongoClient
import pprint
import json

client = MongoClient("mongodb://admin:datarocks@ds143707.mlab.com:43707/heroku_4f1hr8cl")

db = client.heroku_4f1hr8cl

collection = db.mars_scrape

count = collection.count()

print(count)