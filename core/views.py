from django.template import loader
from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def home(request):
	#return HttpResponse("Home Page")
	return render(request, 'core/index.html')