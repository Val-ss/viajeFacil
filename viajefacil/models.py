from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Destino(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=200)
    ubicacion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = "Destino"
    
class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    habitacion = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Hotel"
    
class Reserva_hotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    numero_habitaciones = models.IntegerField()
    numero_huespedes = models.IntegerField()
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=12)
    duracion_reserva = models.DurationField(editable=False)
    tarifa_noche = models.DecimalField(max_digits=10, decimal_places=0)
    def __str__(self):
        return self.nombre_cliente
    
    def save(self, *args, **kwargs):
        # Calcular la duración de la reserva en días
        self.duracion_reserva = self.fecha_salida - self.fecha_entrada
        super().save(*args, **kwargs)
  

    class Meta:
        verbose_name_plural = "Reserva_hotel"

class Seguridad(models.Model): 
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    def __str__(self):
        return self.titulo

    
class Paquete(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    mascota = models.CharField(max_length=100)
    beneficio = models.TextField()
    imagen = models.ImageField(upload_to='home/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    

class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    detalle_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)