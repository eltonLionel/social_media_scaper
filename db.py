import tweepy
import json
from tweepy import Stream
from local_config import *
from pymongo import MongoClient

client = MongoClient('mongodb+srv://m220student:m220password@mflix-cd0uf.mongodb.net/test?retryWrites=true&w=majority')

db = client.tweepydb

res = []
trnd = []

def auth_data():
    auth = tweepy.OAuthHandler(cons_tok, cons_sec)
    auth.set_access_token(app_tok, app_sec)
    twitter_api = tweepy.API(auth)
    return (twitter_api)

def search_data(twitter_api,searchdata = "python"):
    search_results = tweepy.Cursor(twitter_api.search, q=searchdata).items(20)
    for result in search_results:
        res.append(result.text)
    return(res)

def trend_data(twitter_api):
    trends = twitter_api.trends_place(1)
    for trend in trends[0]["trends"]:
        trnd.append(trend['name'])
    return(trnd)

def upload_search(twitter_api):
    search_results = tweepy.Cursor(twitter_api.search, q="python").items(20)
    for result in search_results:
        db['tweets'].insert_one(result._json)

def upload_trend(twitter_api):
    trends = twitter_api.trends_place(1)
    for result in trends[0]["trends"]:
        db['trends'].insert_one(result)