from django.db import models
from django.contrib.auth.models import User
from Card_Game_App.models import PokeType, Pokemon


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(null=True, blank=True)
    species = models.ForeignKey(PokeType, null=True, on_delete=models.SET_NULL)
    coins = models.IntegerField(default=500)

class Card(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='deck')

# class Transcations(models.Model):
#