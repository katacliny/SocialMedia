from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .Core import StartSearch as ss
from .models import UserConfig as uc
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from .form import UpdateUserConfigForm
# Create your views here.

def StartSearch(request):
	print("entra")
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
		
class UpdateUserConfig(UpdateView):
	model = uc
	template_name = "UpdateUserConfig.html"
	form_class = UpdateUserConfigForm
	success_url = "/"

	def get_object(self):
		return uc.objects.first()

	def valid_form(self, form):
		form.save()
		HttpResponseRedirect("Home")
		#return super(self, UpdateConfig).valid_form(form)