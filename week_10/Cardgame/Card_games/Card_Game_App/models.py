from django.db import models


# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    types = models.ManyToManyField('PokeType')
    pokexp = models.CharField(max_length=50)

class PokeType(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.name

