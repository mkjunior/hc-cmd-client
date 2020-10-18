from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def accueil(request):
	return render(request, 'pages/accueil.html')

def shopping(request):
	return render(request, 'pages/shopping.html')

def wishes(request):
	return render(request, 'pages/wishes.html')

def magasin(request):
	return render(request, 'pages/magasin.html')

def setting(request):
	return render(request, 'pages/setting.html')

def contact(request):
	return render(request, 'pages/contact.html')



# Sidebar

def litige(request):
	return render(request, 'pages/litige.html')

def guideuser(request):
	return render(request, 'pages/guideuser.html')

