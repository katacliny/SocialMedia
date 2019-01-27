from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TweetSerializer
from Twitter.models  import Tweet
from rest_framework.generics import ListAPIView


class TweetList(ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer