from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("This is home page")


def eggs(request):
	return HttpResponse("Eggs are 10 pcs!")
