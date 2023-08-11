from django.contrib import admin
from gestionpedidos.models import Acta, Oficial, Pedido, Actividad

class ActaAdmin(admin.ModelAdmin):    
    list_display = ["numero", "inicio_rango_fecha_ejecucion", "final_rango_fecha_ejecucion","estado", "usuario_registro"]
admin.site.register(Acta, ActaAdmin)

class OficialAdmin(admin.ModelAdmin):    
    list_display = ["id", "cedula", "nombre", "estado"]
admin.site.register(Oficial, OficialAdmin)

class ActividadAdmin(admin.ModelAdmin):    
    list_display = ["nombre", ]
admin.site.register(Actividad, ActividadAdmin)

class PedidoAdmin(admin.ModelAdmin):    
    list_display = ["numero", "fecha_registro", 'oficial','actividad', 'acta', 'fecha_ejecucion', 'fecha_registro', 'usuario_registro']
    
admin.site.register(Pedido, PedidoAdmin)