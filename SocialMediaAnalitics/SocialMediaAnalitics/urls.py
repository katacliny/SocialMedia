"""SocialMediaAnalitics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Twitter import views as twitter_views
from main import views as main_views
from django.contrib.auth.decorators import login_required 
from RestAPI.views import TweetList, RegistrationAPI, LoginAPI
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.Login.as_view(), name="Login"),
    path('Logout', main_views.logout_view, name="Logout"),
    path('CreateUser', main_views.CreateUser.as_view(), name="CreateUser"),
    path('Home/', login_required(main_views.Home.as_view()), name="Home"),
    path('UpdateUserConfig/', login_required(main_views.UpdateUserConfig.as_view()), name="UpdateUserConfig"),
    path('StartSearch/', twitter_views.StartSearch),
    path('StopSearch/', twitter_views.StopSearch),
    path('Grafics/', login_required(twitter_views.Grafics.as_view()), name="Grafics"),
    path('HomeTwitter/', login_required(twitter_views.HomeTwitter.as_view()), name="HomeTwitter"),
    path('GetDataForGrafics/', twitter_views.GetDataForGrafics, name="GetDataForGrafics"),
    path('TweetsList/', login_required(twitter_views.TweetsList.as_view()), name="TweetsList"),
    path('CsvFile/', twitter_views.CSVFile, name="CsvFile"),
    path('TweetsListApi/', TweetList.as_view(), name="TweetsListApi"),
    path('api/auth/', include('knox.urls')),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
]
