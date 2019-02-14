from rest_framework import serializers
from rest_framework import viewsets, permissions, generics
from Twitter.models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
	permission_classes = [permissions.IsAuthenticated]
	class Meta:
		model = User
		fields = ['id', 'username']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
	permission_classes = [permissions.IsAuthenticated]
	class Meta:
		model = Tweet
		fields = ['tweeter_user', 'text', 'create', 'hour', 'num_word', 'num_letter', 'tag']
