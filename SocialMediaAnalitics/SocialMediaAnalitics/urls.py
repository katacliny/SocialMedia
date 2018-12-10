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
from django.urls import path
from Twitter import views as twitter_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', twitter_views.Login.as_view(), name="Login"),
    path('Logout', twitter_views.logout_view, name="Logout"),
    path('CreateUser', twitter_views.CreateUser.as_view(), name="CreateUser"),
    path('Home/', login_required(twitter_views.Home.as_view()), name="Home"),
    path('UpdateUserConfig/', login_required(twitter_views.UpdateUserConfig.as_view()), name="UpdateUserConfig"),
    path('StartSearch/', login_required(twitter_views.StartSearch)),
    path('StopSearch/', login_required(twitter_views.StopSearch)),
]
