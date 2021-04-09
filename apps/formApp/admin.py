from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    User,
    Insercion,
    Contrato
    )
# Register your models here.

class InsercionAdmin(admin.ModelAdmin):

    def pdf_actions(self, obj):
        return format_html(
            '<a class="button" href="{}" target="_blank">Genrar PDF Inserción</a>&nbsp;'
            '<a class="button" href="{}" target="_blank">Generar PDF De Contrato</a>',
            reverse('core:pdf-incersion', args=[obj.pk]),
            reverse('core:pdf-contrato', args=[obj.pk]),
        )
    pdf_actions.short_description = 'PDF Actions'
    pdf_actions.allow_tags = True

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
        'pdf_actions',
        'get_matricula',
    )

    def get_matricula(self, obj):
        return obj.datos_del_Vehiculo.matricula
    get_matricula.short_description = 'Matricula'
    get_matricula.admin_order_field = 'datos_del_Vehiculo__matricula'

class ContratoAdmin(admin.ModelAdmin):
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


admin.site.register(User)
admin.site.register(Insercion, InsercionAdmin)
admin.site.register(Contrato, ContratoAdmin)