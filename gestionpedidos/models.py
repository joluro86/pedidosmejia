from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Acta(models.Model):

    ESTADO_ACTA = (
        ('1', 'Activa'),
        ('0', 'Inactiva'),
    )

    numero = models.IntegerField(null=False, primary_key=True)
    inicio_rango_fecha_ejecucion = models.DateField(null=False)
    final_rango_fecha_ejecucion = models.DateField(null=False)
    estado = models.CharField(max_length=20, choices=ESTADO_ACTA, default='1')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_registro = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = 'Acta'
        verbose_name_plural = 'Actas'
        db_table = "Actas"

    def __str__(self):
        return str(self.numero)


class Actividad(models.Model):
    nombre = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        db_table = "Actividades"

    def __str__(self):
        return self.nombre


class Oficial(models.Model):
    ESTADO_OFICIAL = (
        ('1', 'Activo'),
        ('0', 'Inactivo'),
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.IntegerField(unique=True, null=False)
    nombre = models.CharField(max_length=100, null=False)
    estado = models.CharField(
        max_length=20, choices=ESTADO_OFICIAL, default='1')

    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales'
        db_table = "Oficiales"

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    numero = models.IntegerField(unique=True,
        validators=[
            MinValueValidator(10000000, message='Este campo debe tener 8 dígitos.'),
            MaxValueValidator(99999999, message='Este campo debe tener 8 dígitos.'),
            RegexValidator(r'^\d{8}$', message='Este campo debe tener exactamente 8 dígitos.')
        ]
    )
    oficial = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pedidos_as_id_oficial'
    )
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    acta = models.ForeignKey(Acta, on_delete=models.CASCADE)
    fecha_ejecucion = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_registro = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pedidos_as_usuario_registro'
    )

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(self.numero)
