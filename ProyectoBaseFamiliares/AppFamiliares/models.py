from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombreyapellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    nacimiento= models.DateField()