from django.db import models

# Create your models here.


class Alarmas(models.Model):
    nombre = models.CharField(max_length=30)
    foto = models.CharField(max_length=9999999)
    tipo = models.CharField(max_length=60)
    precio = models.IntegerField() 


class Camaras(models.Model):
    nombre = models.CharField(max_length=30)
    foto = models.CharField(max_length=9999999)     
    definicion = models.CharField(max_length=50)
    precio = models.IntegerField() 

class Cercos(models.Model):
    nombre = models.CharField(max_length=30)
    foto = models.CharField(max_length=9999999)     
    voltaje = models.CharField(max_length=50)
    precio = models.IntegerField()   

