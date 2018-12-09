import pandas as pd 
import numpy as np
import tweepy
import sklearn
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
from threading import Thread
from .models import UserConfig as uc
from .models import Tweet
from datetime import datetime
config = uc.objects.first()


class MyListener(StreamListener):
	
	def on_data(self, data):
		if uc.objects.first().is_search:
			json_data = json.loads(data)
			new_tweet = Tweet()
			new_tweet.tweeter_user = json_data["user"]["name"]
			new_tweet.text = json_data["text"]
			new_tweet.create = datetime.now()
			new_tweet.locate = json_data["user"]["location"]
			new_tweet.num_word = json_data["text"].split().__len__()
			new_tweet.num_letter = json_data["text"].__len__()
			new_tweet.save()
			return True
		return False

	def on_error(self, status):
		print(status)
		return True



def StartStream():
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)
	api = tweepy.API(auth)
	listener = MyListener()
	twitter_stream = Stream(auth, listener)
	twitter_stream.filter(track=[uc.objects.first().filter_key])


def StartSearch():
	thread = Thread(target=StartStream)
	thread.start()