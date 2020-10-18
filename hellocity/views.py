from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request, 'accueil.html')

def login(request):
	pass

def register(request):
	pass