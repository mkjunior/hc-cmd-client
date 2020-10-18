from django.db import models

# Create your models here.


class Client(models.Model):
    nom = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class Etiquette(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    CATEGORIE = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Enfant', 'Enfant'),
    )
    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(null=True)
    categorie = models.CharField(max_length=200, null=True, choices=CATEGORIE)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    etiquettes = models.ManyToManyField(Etiquette)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    STATUS = (
        ('En attente', 'En attente'),
        ('En cours de livraison', 'En cours de livraison'),
        ('Livré', 'Livré'),
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)