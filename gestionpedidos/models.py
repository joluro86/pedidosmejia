from django.db import models

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
        verbose_name_plural = 'Acta'
        db_table = "Actas"

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre= models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        db_table = "Actividades"

    def __str__(self):
        return self.nombre

class Oficial(models.Model):
    nombre= models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales'
        db_table = "Oficiales"

    def __str__(self):
        return self.nombre

