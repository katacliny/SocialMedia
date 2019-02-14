from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .Core import StartSearch as ss
from main.models import UserConfig as uc
from .models import Tweet as tw
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import ListView
from main.form import UpdateUserConfigForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import json
import random
import csv
from datetime import datetime
from SocialMediaAnalitics.settings import STATICFILES_DIRS
import os
# Create your views here.


class HomeTwitter(TemplateView):
	template_name = "HomeTwitter.html"

	def get_context_data(self, **kwargs):
	    data = super().get_context_data(**kwargs)
	    data['listen'] = uc.objects.filter(user = self.request.user).first().is_search
	    return data

def StartSearch(request):
	if request.user.is_authenticated:
		config = uc.objects.filter(user = request.user).first()
		config.is_search = True
		config.save()
		ss(request.user)
	return JsonResponse({'status': "done"})

def StopSearch(request):
	config = uc.objects.filter(user = request.user).first()
	config.is_search = False
	config.save()
	return JsonResponse({'status': "done"})


class Grafics(TemplateView):
	template_name = "Grafics.html"

	def get_context_data(self, **kwargs):
	    data = super().get_context_data(**kwargs)
	    data['listen'] = uc.objects.filter(user = self.request.user).first().is_search
	    return data

def GetDataForGrafics(request):
	data = {}
	databynum_word = {}
	databynum_letter = {}
	databydate = {}
	databyhour = {}
	res = {}
	if request.is_ajax():
		alltwbytag = tw.objects.filter(user = request.user).order_by('tag')
		count = {}
		for tw_ in alltwbytag:
			if tw_.tag not in count.keys():
				count[tw_.tag] = 1
			else:
				count[tw_.tag] += 1
		
		data['type'] = "bar"
		data['data'] = {
			"labels": list(count.keys()),
			"datasets": [{
	            "label": 'Tweets por hashtag',
	            "data": list(count.values()),
	            "backgroundColor": ["rgba({}, {}, {}, {})".format(
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256),256) for i in range(0, list(count.keys()).__len__())],
	            "borderColor": [
	                
	            ],
	            "borderWidth": 1
	        }]
		}
		data['options']= {
	        "scales": {
	            "yAxes": [{
	                "ticks": {
	                    "beginAtZero":True
	                }
	            }]
	        }
		}

		alltwbynum_word = tw.objects.filter(user = request.user).order_by('num_word')
		count = {}
		for tw_ in alltwbynum_word:
			if tw_.num_word not in count.keys():
				count[tw_.num_word] = 1
			else:
				count[tw_.num_word] += 1
		
		databynum_word['type'] = "bar"
		databynum_word['data'] = {
			"labels": list(count.keys()),
			"datasets": [{
	            "label": '# de tweets con esta cantidad de palabras',
	            "data": list(count.values()),
	            "backgroundColor": ["rgba({}, {}, {}, {})".format(
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256),256) for i in range(0, list(count.keys()).__len__())],
	            "borderColor": [
	                
	            ],
	            "borderWidth": 1
	        }]
		}
		databynum_word['options']= {
	        "scales": {
	            "yAxes": [{
	                "ticks": {
	                    "beginAtZero":True
	                }
	            }]
	        }
		}


		alltlbynum_letter = tw.objects.filter(user = request.user).order_by('num_letter')
		count = {}
		for tl_ in alltlbynum_letter:
			if tl_.num_letter not in count.keys():
				count[tl_.num_letter] = 1
			else:
				count[tl_.num_letter] += 1
		
		databynum_letter['type'] = "bar"
		databynum_letter['data'] = {
			"labels": list(count.keys()),
			"datasets": [{
	            "label": '# de tweets con esta cantidad de letras en los tweets',
	            "data": list(count.values()),
	            "backgroundColor": ["rgba({}, {}, {}, {})".format(
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256),256) for i in range(0, list(count.keys()).__len__())],
	            "borderColor": [
	                
	            ],
	            "borderWidth": 1
	        }]
		}
		databynum_letter['options']= {
			"responsive": True,
		}

		alltlbydate = tw.objects.filter(user = request.user).order_by('create')
		count = {}
		for tl_ in alltlbydate:
			if tl_.create not in count.keys():
				count[tl_.create] = 1
			else:
				count[tl_.create] += 1
		
		databydate['type'] = "line"
		databydate['data'] = {
			"labels": list(count.keys()),
			"datasets": [{
	            "label": '# por fechas',
	            "data": list(count.values()),
	            "backgroundColor": ["rgba({}, {}, {}, {})".format(
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256),256) for i in range(0, list(count.keys()).__len__())],
	            "borderColor": [
	                
	            ],
	            "borderWidth": 1
	        }]
		}
		databydate ['options']= {
			"responsive": True,
		}

		alltlbyhour = tw.objects.filter(user = request.user).order_by('hour')
		count = {}
		for tl_ in alltlbyhour:
			if tl_.hour not in count.keys():
				count[tl_.hour] = 1
			else:
				count[tl_.hour] += 1
		
		databyhour['type'] = "bar"
		databyhour['data'] = {
			"labels": list(count.keys()),
			"datasets": [{
	            "label": '# por horas',
	            "data": list(count.values()),
	            "backgroundColor": ["rgba({}, {}, {}, {})".format(
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256), 
	            	random.randrange(150, 256),256) for i in range(0, list(count.keys()).__len__())],
	            "borderColor": [
	                
	            ],
	            "borderWidth": 1
	        }]
		}
		databyhour ['options']= {
			"responsive": True,
		}

		res["bytag"] = data
		res["num_word"] = databynum_word
		res["num_letter"] = databynum_letter
		res["date"] = databydate 
		res["hour"] = databyhour

	return JsonResponse(res)
    	

class TweetsList(ListView):
    model = tw
    template_name = 'TweetList.html' 
    context_object_name = 'tweets' 
    paginate_by = 10

    def get_queryset(self):
        qs = tw.objects.filter(user = self.request.user).order_by('tag')
        return qs

def CSVFile(request):
	filedir = os.path.join(csvdirs, 'Summary-' + str(datetime.now().date()) + ".csv")

	with open(str(filedir), 'w') as file:
		filewriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(["Twitter User", "Texto", "Fecha de Creado", "Hora", "Región", "Número de palabras", "Número de letras", "App Username", "Tag"])

	with open(str(filedir), 'a') as file:
		filewriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for tweet in tw.objects.filter(user = request.user).order_by('create'):
		    filewriter.writerow([str(tweet.tweeter_user).encode(encoding='UTF-8',errors='strict'), 
		    					 str(tweet.text).encode(encoding='UTF-8',errors='strict'), 
		    					 str(tweet.create).encode(encoding='UTF-8',errors='strict'), 
		    					 str(tweet.hour).encode(encoding='UTF-8',errors='strict'), 
		    					 str(tweet.locate).encode(encoding='UTF-8',errors='strict'), 
		    					 str(tweet.num_word).encode(encoding='UTF-8',errors='strict'), 
		    					 str(tweet.num_letter).encode(encoding='UTF-8',errors='strict'),
								 str(tweet.user.username).encode(encoding='UTF-8',errors='strict'), 
								 str(tweet.tag).encode(encoding='UTF-8',errors='strict')])
	with open(str(filedir), 'r') as file:

		response = HttpResponse(file, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=Tweet List.csv'
		return response

    
  
