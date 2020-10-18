from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from . models import *
from .forms import CmdForm
# Create your views here.


def dashboard(request):
	commande = Commande.objects.all()
	client = Client.objects.all()

	total_client = client.count()
	total_commande = commande.count()
	 
	livre = commande.filter(status='Livré').count()
	attente = commande.filter(status='En attente').count()


	context = {'commande':commande, 'client':client, 'total_client':total_client,
	'livre':livre, 'attente':attente, 'total_commande':total_commande}
	
	return render(request, 'pages/dashboard.html', context)
 
def produit(request):
	produit = Produit.objects.all()

	return render(request, 'pages/produit.html', {'produits':produit})

def client(request, pk):
	client = Client.objects.get(id=pk)
	commande = client.commande_set.all()
	total_cmd = commande.count()

	context = {'client':client, 'commande':commande, 'total_cmd':total_cmd}
	return render(request, 'pages/client.html', context)

def creerCmd(request):

	form = CmdForm()
	if request.method == 'POST':
		form = CmdForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/dashboard')

	context={'form':form, 'client':client}
	return render(request, 'pages/cmd_form.html', context)

def modifierCmd(request, pk):

	cmd = Commande.objects.get(id=pk)
	form = CmdForm(instance=cmd)

	if request.method == 'POST':
		form = CmdForm(request.POST, instance=cmd)
		if form.is_valid():
			form.save()
			return redirect('/dashboard')

	context={'form':form}
	return render(request, 'pages/cmd_form.html', context)

def suppCmd(request, pk):
	cmd = Commande.objects.get(id=pk)
	if request.method == 'POST':
		cmd.delete()
		return redirect('/dashboard')
	context={'item':cmd}
	return render(request, 'pages/delete.html', context)