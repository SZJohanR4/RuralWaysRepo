from django.contrib.auth.models import User
from administrador.models import Ofertas
from agricultor.models import Tipos_Productos
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
    idUsuario=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Noticias(models.Model):
    titulo=models.CharField(max_length=100)
    fecha=models.DateField()
    contenido=models.TextField()
    imagen=models.CharField(max_length=100)
    idPropietario=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Carrito_Compras(models.Model):
    cantidad=models.IntegerField()
    valor=models.DecimalField(max_digits=5, decimal_places=2)
    idUsuario=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class Factura(models.Model):
    valorTotal=models.DecimalField(max_digits=5, decimal_places=2)
    estado=models.CharField(max_length=100)
    direccionEnvio=models.CharField(max_length=100)
    
    idCliente=models.ForeignKey(User, related_name='cliente',on_delete=models.CASCADE)
    idTransportador=models.ForeignKey(User,related_name='transportador',on_delete=models.CASCADE)
    idCarrito=models.ForeignKey(Carrito_Compras,on_delete=models.CASCADE)
    
class Productos(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    estado=models.CharField(max_length=100)
    
    idOferta=models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipos_Productos, on_delete=models.CASCADE)
    idPropietario=models.ForeignKey(User, on_delete=models.CASCADE)
    
class Carrito_por_Productos(models.Model):
    idCarrito=models.ForeignKey(Carrito_Compras,on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Productos,on_delete=models.CASCADE)
    
    
class Imagenes_Productos(models.Model):
    imagen=models.CharField(max_length=300)#supongo que es el link de la imagen
    descripcion=models.CharField(max_length=300)
    
    idProducto=models.ForeignKey(Productos, on_delete=models.CASCADE)