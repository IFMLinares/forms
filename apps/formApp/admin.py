from django.contrib import admin
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from .models import (
    User,
    Insercion,
    Contrato,
    DatosVehiculo.
    Suplemento,
    DatosComprador,
    Documentacion,
    Mantenimiento,
    ExamenVisual
    )
# Register your models here.

class InsercionResource(resources.ModelResource):
    class Meta:
        model = Insercion

class ContratoResource(resources.ModelResource):
    class Meta:
        model = Contrato

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = User

class InsercionAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    resource_class = InsercionResource

    readonly_fields = (
        'datos_del_Vehiculo',
        'suplementos',
        'datos_del_comprador',
        'documentacion',
        'mantenimiento',
        'examen_visual'
    )
    search_fields = [
        'datos_del_Vehiculo__matricula',
    ]
    list_display = (
        'concesionario',
        'get_matricula',
        'get_marca',
        'get_modelo',
        'pdf_actions',
    )

    def get_matricula(self, obj):
        return obj.datos_del_Vehiculo.matricula
    get_matricula.short_description = 'Matricula'
    get_matricula.admin_order_field = 'datos_del_Vehiculo__matricula'

    def get_marca(self, obj):
        return obj.datos_del_Vehiculo.marca
    get_marca.short_description = 'Marca'
    get_marca.admin_order_field = 'datos_del_Vehiculo__marca'

    def get_modelo(self, obj):
        return obj.datos_del_Vehiculo.modelo
    get_modelo.short_description = 'modelo'
    get_modelo.admin_order_field = 'datos_del_Vehiculo__modelo'

    def pdf_actions(self, obj):
        return format_html(
            '<a class="button" href="{}" target="_blank">Inserción</a>&nbsp;'
            '<a class="button" href="{}" target="_blank">COMPRAVENTA</a>',
            reverse('core:pdf-incersion', args=[obj.pk]),
            reverse('core:pdf-contrato', args=[obj.pk]),
        )
    pdf_actions.short_description = 'IMPRIMIR'
    pdf_actions.allow_tags = True

class ContratoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ContratoResource

    readonly_fields = (
        'usuario',
        'contratoLocales',
        'fecha',
        'firmante',
        'nacido',
        'fechaNacimiento',
        'residenciaSede',
        'telefono',
        'profesion',
        'CifNif',
        'vendedor',
        'marca',
        'version',
        'modelo',
        'bastidor',
        'estadoEncontrado',
        'estadoEncontradoDescripcion',
        'marceEmpresa',
        'versionEmpresa',
        'modeloEmpresa',
        'bastidorEmpresa',
        'fechaPrimeraMatriculacion',
        'equivalenteAcordado',
        'equivalenteAcordadoMonto',
        'abonadoComprador',
        'abonadoCompradorMonto',
        'PrecioAcordado',
        'valorVehiculoRetirado',
        'depostoGarantiaPagado',
        'sociedadFinanciera',
        'nroProtocolo',
        'importaFinanciado',
        'gastosInstruccionSello',
        'nroPlazos',
        'importePlazos',
        'lugar',
        'fecha2',
        'total'
    )
    list_display = (
        'usuario',
        'contratoLocales',
        'marca',
        'modelo',
    )

# class UsuarioAdmin(admin.ModelAdmin):
#     change_form_template = 'index.html'

#     def get_osm_info(self):
#         # ...
#         pass

#     def change_view(self, request, object_id, form_url='index.html', extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['osm_data'] = self.get_osm_info()
#         return super().change_view(
#             request, object_id, form_url, extra_context=extra_context,
#         )

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UsuarioResource

admin.site.register(User, UserAdmin)
admin.site.register(Insercion, InsercionAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(DatosVehiculo)
admin.site.register(Suplemento)
admin.site.register(DatosComprador)
admin.site.register(Documentacion)
admin.site.register(Mantenimiento)
admin.site.register(ExamenVisual)