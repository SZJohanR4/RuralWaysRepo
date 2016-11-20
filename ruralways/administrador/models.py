from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Ofertas(models.Model):
    
    tipo=models.CharField(max_length=100)
    valor=models.DecimalField(max_digits=5, decimal_places=2)#puede ser float
    descuento=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    #fecha_vencimiento=models.DateField()
    duracion=models.DateField()
    
class Solicitudes(models.Model):
    solicitud=models.CharField(max_length=300)
    idUsuarioRem=models.ForeignKey(User, related_name='usuarioRemSol',on_delete=models.CASCADE)
    idUsuarioDest=models.ForeignKey(User,related_name='usuarioDestSol', on_delete=models.CASCADE)
    
    
class Chat(models.Model):
    Pregunta=models.CharField(max_length=300)
    Respuesta=models.CharField(max_length=300)
    idSolicitud=models.ForeignKey(Solicitudes, on_delete=models.CASCADE)