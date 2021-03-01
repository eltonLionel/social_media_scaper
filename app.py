from flask import Flask, request, render_template
import json
from bson import json_util
from db import *
import pyfacebook
from fb_config import*

lst = []

# instantiate the Flask app.
app = Flask(__name__)

# This is the / route, or the main landing page route.
@app.route("/")
def main():
	# we will use Flask's render_template method to render a website template.
    return render_template("homepage.html")

@app.route("/facebook")
def facebook():
	# we will use Flask's render_template method to render a website template.
    return render_template("Facebook.html")

@app.route("/flive")
def live():
	access_token='EAAEJnIZA2ks0BAKKOwQ0TTYPfA8ubBzbTVmkZCA2AvvL3HZBtGZCJ8DmAg3Y3Kp81ZA788UZAThVZAqwu3HKObjd95kms1EZBGj4EXdymAmfMrHkZCw5dXtMurNXFmGpybn9LV9imsXiI2YN9TUwowKBHm6fsSV5jPvoEt7MhBTo6kmPllYBq0Xucjl5X4MiOZAPVlxJkdq3ckqgZDZD'

	api = pyfacebook.Api(app_id=apps_id, app_secret=apps_secret, short_token=access_token)

	a = api.get_page_feeds('110473587383626')

	return render_template("flive.html",dump = a)


@app.route("/twitter")
def twitter():
	# we will use Flask's render_template method to render a website template.
    return render_template("twitter.html")

@app.route("/ttrending")
def trend():
	apis = auth_data()

	trnd = trend_data(apis)

	return render_template("ttrending.html",dump = trnd)

@app.route("/ttrending/upload")
def trend_upload():
	apis = auth_data()

	upload_trend(apis)

	return render_template("ttrending.html",dump = ["Successful!",""])


@app.route("/tsearch")
def search():
	return render_template ("tsearch.html")

@app.route("/tsearchdata",methods = ['POST'])
def search_tweets():

	searchdata = str(request.form['search'])

	apis = auth_data()

	res = search_data(apis,searchdata)

	return render_template("tsearchtweets.html",newlist = res)

@app.route("/tsearchdata/upload")
def search_upload():
	
	apis = auth_data()

	upload_search(apis)

	searchdata = ""

	return render_template("tsearchtweets.html",newlist = ["Successful!",""])

# run the flask app.

if __name__ == "__main__":

	app.run(debug=True)
	
