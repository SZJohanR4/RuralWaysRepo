from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Tipos_Productos(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    

