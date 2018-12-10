from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .Core import StartSearch as ss
from .models import UserConfig as uc
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import FormView
from django.views.generic import CreateView
from .form import UpdateUserConfigForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("Login"))

class Login(FormView):
	form_class = AuthenticationForm
	success_url = "/"
	template_name = "Login.html"

	def form_valid(self, form):
	    username = self.request.POST['username']
	    password = self.request.POST['password']
	    user = authenticate(self.request, username=username, password=password)
	    if user is not None:
	        login(self.request, user)
	       	return HttpResponseRedirect(reverse_lazy("Home"))
	    else:
	        return HttpResponseRedirect(reverse_lazy("Login"))

def StartSearch(request):
	config = uc.objects.first()
	config.is_search = True
	config.save()
	ss()
	return HttpResponse("Start")

def StopSearch(request):
	config = uc.objects.first()
	config.is_search = False
	config.save()
	return HttpResponse("Stop")

class Home(TemplateView):
	template_name = "Home.html"
	
class CreateUser(CreateView):
	model = User
	form_class = UserCreationForm
	success_url = "Login"	
	template_name = "Login.html"
	extra_context = {"create": True}

	def form_valid(self, form):
	    if form.is_valid():
	    	new_tweet = uc()
	    	user = form.save()
	    	new_tweet.user = user
	    	new_tweet.save()
	    return HttpResponseRedirect(reverse_lazy("Login"))

class UpdateUserConfig(UpdateView):
	model = uc
	template_name = "UpdateUserConfig.html"
	form_class = UpdateUserConfigForm
	success_url = "/"

	def get_object(self):
		return uc.objects.first()

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(reverse_lazy("Home"))
		#return super(UpdateConfig, self).valid_form(form)