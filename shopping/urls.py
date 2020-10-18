from django.urls import path

from . import views

app_name = 'shopping'

urlpatterns = [

    path('', views.accueil, name="accueil"),
    path('accueil/', views.accueil, name="accueil"),
    path('shopping/', views.shopping, name="shopping"),
    path('wishes/', views.wishes, name="wishes"),
    path('magasin/', views.magasin, name="magasin"),
    path('setting/', views.setting, name="setting"),
    path('contact/', views.contact, name="contact"),




    path('litige/', views.litige, name="litige"),
    path('guideuser/', views.guideuser, name="guideuser"),

]