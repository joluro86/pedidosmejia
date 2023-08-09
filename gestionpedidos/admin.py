from django.contrib import admin
from gestionpedidos.models import Acta, Oficial

class ActaAdmin(admin.ModelAdmin):    
    list_display = ["numero", "inicio_rango_fecha_ejecucion", "final_rango_fecha_ejecucion","estado", "usuario_registro"]
admin.site.register(Acta, ActaAdmin)

class OficialAdmin(admin.ModelAdmin):    
    list_display = ["id", "cedula", "nombre", "estado"]
admin.site.register(Oficial, OficialAdmin)