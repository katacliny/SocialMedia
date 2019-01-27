from rest_framework import serializers
from Twitter.models import Tweet



class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ('tweeter_user', 'text', 'create', 'hour', 'num_word', 'num_letter', 'tag')
