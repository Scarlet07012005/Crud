from django.db import models

class Aprendices(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    documento = models.PositiveIntegerField()
    typeDocumento = models.CharField(max_length=3)
    ficha = models.PositiveIntegerField()
