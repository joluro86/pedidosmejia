from django.db import models
from django.contrib.auth.models import AbstractUser

class Acta(models.Model):

    ESTADO_ACTA = (
        ('1', 'Activa'),
        ('0', 'Inactiva'),
    )

    numero= models.IntegerField(null=False, primary_key=True)
    inicio_rango_fecha_ejecucion = models.DateField(null=False)
    final_rango_fecha_ejecucion = models.DateField(null=False)
    estado = models.CharField(max_length=20, choices=ESTADO_ACTA, default='1')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=200, null=False, default="1") # ESTO SE CAMBIARA OJO


    class Meta:
        verbose_name = 'Acta'
        verbose_name_plural = 'Actas'
        db_table = "Actas"
     

    def __str__(self):
        return str(self.numero)

class Actividad(models.Model):
    nombre= models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        db_table = "Actividades"

    def __str__(self):
        return self.nombre
    
class CustomUser(AbstractUser):
    cedula = models.CharField(max_length=20, default=100) 

class Oficial(models.Model):
    ESTADO_OFICIAL = (
        ('1', 'Activo'),
        ('0', 'Inactivo'),
    )
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cedula = models.IntegerField(unique=True, null=False)
    nombre= models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=20, choices=ESTADO_OFICIAL, default='1')

    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales'
        db_table = "Oficiales"

    def __str__(self):
        return self.nombre

