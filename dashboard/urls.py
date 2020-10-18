from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'dashboard'

urlpatterns = [

    path('', views.dashboard, name="dashboard"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('produit/', views.produit, name="produit"),

    path('client/<str:pk>/', views.client, name="client"), 

    path('creer_cmd/', views.creerCmd, name="creer_cmd"),  
    path('modifier_cmd/<str:pk>/', views.modifierCmd, name="modifier_cmd"),  
    path('delete_cmd/<str:pk>/', views.suppCmd, name="supprimer_cmd"),  

]
