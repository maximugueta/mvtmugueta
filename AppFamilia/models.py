from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    nacimiento=models.DateField()
