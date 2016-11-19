from django.contrib.auth.models import User
from agricultor.models import Productos
from django.db import models
# Create your models here.
class Perfil(models.Model):
    id_auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    tipo_documento=models.CharField(max_length=100)#poner campo en el diagrama
    documento=models.IntegerField()
    telefono=models.IntegerField()
    celular=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)
    codigoPostal=models.CharField(max_length=100)
    placaCarro=models.CharField(max_length=100)
    rol=models.CharField(max_length=100)#para saber con que rol se logea
    
    
class Logs(models.Model):
    tipo=models.CharField(max_length=100)
    informacion=models.CharField(max_length=100)
    idUsuario=models.ForeignKey(Perfil,on_delete=models.CASCADE)
    
class Noticias(models.Model):
    titulo=models.CharField(max_length=100)
    fecha=models.DateField()
    contenido=models.TextField()
    imagen=models.CharField(max_length=100)
    idPropietario=models.ForeignKey(Perfil,on_delete=models.CASCADE)
    
class Carrito_Compras(models.Model):
    cantidad=models.IntegerField()
    valor=models.DecimalField()
    idUsuario=models.ForeignKey(Perfil,on_delete=models.CASCADE)
    
    
class Factura(models.Model):
    valorTotal=models.DecimalField()
    estado=models.CharField(max_length=100)
    direccionEnvio=models.CharField(max_length=100)
    
    idCliente=models.ForeignKey(Perfil,on_delete=models.CASCADE)
    idTransportador=models.ForeignKey(Perfil,on_delete=models.CASCADE)
    idCarrito=models.ForeignKey(Carrito_Compras,on_delete=models.CASCADE)
    
class Carrito_por_Productos(models.Model):
    idCarrito=models.ForeignKey(Carrito_Compras,on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Productos,on_delete=models.CASCADE)