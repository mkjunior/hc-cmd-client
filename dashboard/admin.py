from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Etiquette)
admin.site.register(Commande)