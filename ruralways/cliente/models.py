from usuario.models import Productos
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Preguntas_Producto(models.Model):
    pregunta=models.TextField()
    respuesta=models.TextField()
    idProducto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    idUsuarioRemitente=models.ForeignKey(User, related_name='usuarioRemitenPre', on_delete=models.CASCADE)
    idUsuarioDestino=models.ForeignKey(User, related_name='usuarioDestinoPre', on_delete=models.CASCADE)