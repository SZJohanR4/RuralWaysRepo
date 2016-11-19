from usuario.models import Perfil
from agricultor.models import Productos
from django.db import models
# Create your models here.

class Preguntas_Producto(models.Model):
    pregunta=models.TextField()
    respuesta=models.TextField()
    idProducto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    idUsuarioRemitente=models.ForeignKey(Perfil, on_delete=models.CASCADE)
    idUsuarioDestino=models.ForeignKey(Perfil, on_delete=models.CASCADE)