import pandas as pd 
import numpy as np
import tweepy
import sklearn
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
from threading import Thread
from main.models import UserConfig as uc
from .models import Tweet
from datetime import datetime
from dateutil.parser import parse
config = uc.objects.first()


class MyListener(StreamListener):

	def __init__(self, user, *args, **kwargs):
		tweepy.StreamListener.__init__(self)
		self.user = user
	
	def on_data(self, data):
		if uc.objects.filter(user = self.user).first().is_search:
			try:
				json_data = json.loads(data)
				new_tweet = Tweet()
				new_tweet.tweeter_user = json_data["user"]["name"]
				new_tweet.text = str(json_data["text"])
				new_tweet.create = parse(json_data["created_at"], fuzzy=True)
				new_tweet.hour = parse(json_data["created_at"], fuzzy=True).hour
				new_tweet.locate = json_data["user"]["location"]
				new_tweet.num_word = json_data["text"].split().__len__()
				new_tweet.num_letter = json_data["text"].__len__()
				new_tweet.user = self.user
				new_tweet.tag = uc.objects.filter(user = self.user).first().filter_key
				new_tweet.save()
			except Exception as e:
				print(e)
				print("Error al guardar ")
			return True
		return False

	def on_error(self, status):
		print(status)
		return True



def StartStream(*args, **kwargs):
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)
	api = tweepy.API(auth)
	listener = MyListener(args[0])
	twitter_stream = Stream(auth, listener)
	twitter_stream.filter(track=[uc.objects.filter(user = args[0]).first().filter_key])


def StartSearch(user):
	if uc.objects.filter(user = user).first().is_search:
		thread = Thread(target=StartStream, args=[user])
		thread.start()