from administrador.models import Ofertas
from usuario.models import Perfil
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Tipos_Productos(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    
class Productos(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    estado=models.CharField(max_length=100)
    
    idOferta=models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipos_Productos, on_delete=models.CASCADE)
    idPropietario=models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
class Imagenes_Productos(models.Model):
    imagen=models.CharField(max_length=300)#supongo que es el link de la imagen
    descripcion=models.CharField(max_length=300)
    
    idProducto=models.ForeignKey(Productos, on_delete=models.CASCADE)