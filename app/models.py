from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    email = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    
