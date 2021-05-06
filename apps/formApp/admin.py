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
        'get_matricula',
        'get_marca',
        'get_modelo',
        'concesionario',
        'get_fecha_insercion',
        'visualizar',
        'pdf_actions',
    )
    list_per_page = 50

    # fieldsets = (
    #     ("DATOS DEL VEHICULO", {'fields': ['datos_del_Vehiculo',]}),
    # )

    def get_matricula(self, obj):
        return obj.datos_del_Vehiculo.matricula
    get_matricula.short_description = 'Matricula'
    get_matricula.admin_order_field = 'datos_del_Vehiculo__matricula'

    def get_fecha_insercion(self, obj):
        return obj.datos_del_Vehiculo.fecha_entrega
    get_fecha_insercion.short_description = 'Fecha de Insercion'
    get_fecha_insercion.admin_order_field = 'datos_del_Vehiculo__fecha_entrega'

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
            '<a class="button" href="{}" target="_blank">Inserción</a>&nbsp;',
            # '<a class="button" href="{}" target="_blank">Compraventa</a>',
            reverse('core:pdf-incersion', args=[obj.pk]),
            # reverse('core:pdf-contrato', args=[obj.pk]),
        )
    pdf_actions.short_description = 'IMPRIMIR'
    pdf_actions.allow_tags = True

    def visualizar(self, obj):
        return format_html(
            '<span style="padding-left: 18%;"></span><a class="button" href="{}" style="padding: 0; padding-left 1px;">&nbsp;&nbsp;&nbsp;<span class="sidebar-link-icon changelink"></span></a>',
            reverse('admin:formApp_insercion_change', args=[obj.pk])
        )
    visualizar.short_description = 'VISUALIZAR'
    visualizar.allow_tags = True

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

    list_per_page = 50

admin.site.register(User)
admin.site.register(Insercion, InsercionAdmin)
admin.site.register(Contrato, ContratoAdmin)