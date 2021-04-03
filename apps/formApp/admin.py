from django.contrib import admin
from .models import (
    User, 
    Form, 
    DatosVehiculo, 
    Suplemento, 
    DatosComprador, 
    Documentacion, 
    Mantenimiento,
    ExamenVisual)
# Register your models here.

class FormAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datos_del_Vehiculo',
        'suplementos',
        'datos_del_comprador',
        'documentacion',
        'mantenimiento',
        'examen_visual'
    )
    search_fields = [
        'datos_del_Vehiculo__matricula'
    ]
    
    list_display = (
        'concesionario',
        'get_matricula'
    )

    def get_matricula(self, obj):
        return obj.datos_del_Vehiculo.matricula
    get_matricula.short_description = 'Matricula'
    get_matricula.admin_order_field = 'datos_del_Vehiculo__matricula'

admin.site.register(User)
admin.site.register(Form, FormAdmin)
# admin.site.register(DatosVehiculo)
# admin.site.register(Suplemento)
# admin.site.register(DatosComprador)
# admin.site.register(Documentacion)
# admin.site.register(Mantenimiento)
# admin.site.register(ExamenVisual)