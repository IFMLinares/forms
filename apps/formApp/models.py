from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

def boleanoString(boleano):
    if boleano == True:
        return 'Si'
    else:
        return 'No'

class User(AbstractUser):
    phone = models.CharField(max_length=12)
    nombre_Razon_Social = models.CharField(max_length=60)
    nro_IDentificación_Fiscal_NIF = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    codigo_postal = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to = 'users', blank=True, null=True)

    class Meta:
        db_table = 'auth_user'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class DatosVehiculo(models.Model):
    matricula = models.CharField(max_length=240,blank=True, null=True)
    transmision = models.CharField(max_length=240,blank=True, null=True)
    marca = models.CharField(max_length=240,blank=True, null=True)
    modelo = models.CharField(max_length=240,blank=True, null=True)
    alimentacion = models.CharField(max_length=240,blank=True, null=True)
    clase_de_cont = models.CharField(max_length=240,blank=True, null=True) #clase de control
    prime_matr  = models.CharField(max_length=240,blank=True, null=True) #primera matricula
    version = models.CharField(max_length=240,blank=True, null=True)
    bastidor = models.CharField(max_length=240,blank=True, null=True)
    potencia_KW = models.CharField(max_length=240,blank=True, null=True)
    nro_propietarios_Privados  = models.CharField(max_length=240,blank=True, null=True)
    nro_propietarios_profesionales = models.CharField(max_length=240,blank=True, null=True)
    cilindrada = models.CharField(max_length=240,blank=True, null=True)
    color = models.CharField(max_length=240,blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_activacion = models.DateField(blank=True, null=True)

    def __str__(self):
        retornar = 'Matricula ' + self.matricula + '\n Transmisión: '+ self.transmision  + '\n Marca: ' + self.marca + '\n Modelo: ' + self.modelo + '\n Alimentacion: ' + self.alimentacion + '\n clase de cont: ' + self.clase_de_cont + '\n Primer matricula: ' + self.prime_matr + '\n potencia_KW: ' + self.potencia_KW + '\n nro propietarios Privados: ' + self.nro_propietarios_Privados + '\n nro propietarios profesionales: ' + self.nro_propietarios_profesionales + '\n cilindrada: ' + self.cilindrada + '\n color: ' + self.color + '\n fecha_entrega: ' + self.fecha_entrega.strftime('%d/%m/%Y') + '\n fecha_inicio: ' + self.fecha_inicio.strftime('%d/%m/%Y') + '\n fecha_activacion: ' + self.fecha_activacion.strftime('%d/%m/%Y')
        return retornar

    class Meta:
        verbose_name = "Datos del vehiculo"
        verbose_name_plural = "Datos de los vehiculos"

class Suplemento(models.Model):
    cuatro_por_cuatro = models.BooleanField(blank=True, null=True)
    super_Car = models.BooleanField(blank=True, null=True)
    cambio_autom = models.BooleanField(blank=True, null=True)
    suv = models.BooleanField(blank=True, null=True)
    vehiculo_comercial = models.BooleanField(blank=True, null=True)
    cobertura = models.BooleanField(blank=True, null=True)

    def __str__(self):
        retornar = '4x4: ' + boleanoString(self.cuatro_por_cuatro) + '\n Super car: ' + boleanoString(self.super_Car) + '\n Cambio automatico: ' + boleanoString(self.cambio_autom) + '\n Suv: ' + boleanoString(self.suv) + '\n Vehículo comercial: ' + boleanoString(self.vehiculo_comercial) + '\n +Cobertura: ' + boleanoString(self.cobertura)
        return retornar

class DatosComprador(models.Model):
    nombre_Completo = models.CharField(max_length=240, blank=True, null=True)
    codigo_postal = models.CharField(max_length=240, blank=True, null=True)
    localidad_Provincia_Pais = models.CharField(max_length=240, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=240, blank=True, null=True)
    numero_de_telefono  = models.CharField(max_length=240, blank=True, null=True)
    numero_de_movil = models.CharField(max_length=240, blank=True, null=True)
    documento_identidad = models.CharField(max_length=240, blank=True, null=True)

    def __str__(self):
        retornar = 'Nombre completo: ' + self.nombre_Completo + '\n Código Postal: ' +  self.codigo_postal + '\n Localidad/Provincia/País: ' + self.localidad_Provincia_Pais + '\n Email: ' + self.email + '\n Dirección: ' + self.direccion + '\n Número de telefono: ' + self.numero_de_telefono + '\n Número Móvil: ' + self.numero_de_movil + '\n Documento de Identidad: ' + self.documento_identidad
        return retornar

class Documentacion(models.Model):
    rueda_repuesto1 = models.BooleanField(blank=True, null=True)
    duplicado_llaves = models.BooleanField(blank=True, null=True)
    kit_inflado = models.BooleanField(blank=True, null=True)
    triangulo_emergencia = models.BooleanField(blank=True, null=True)
    gato = models.BooleanField(blank=True, null=True)
    chaleco_alta_visibilidad = models.BooleanField(blank=True, null=True)
    kit_bombillas = models.BooleanField(blank=True, null=True)
    kit_bombillas_fusibles = models.BooleanField(blank=True, null=True)
    cod_card = models.BooleanField(blank=True, null=True)
    libre_uso_mantenimiento = models.BooleanField(blank=True, null=True)
    ficha_tecnica = models.BooleanField(blank=True, null=True)
    permiso_circulacion = models.BooleanField(blank=True, null=True)

    itv = models.CharField(max_length=240)
    fecha = models.DateField()

    def __str__(self):
        retornar = 'Rueda de Repuesto 1: ' + boleanoString(self.rueda_repuesto1) + '\n Kit de Inflado: ' + boleanoString(self.kit_inflado) + '\n Triángulo de emergencia: ' + boleanoString(self.triangulo_emergencia)  + '\n Gato: ' + boleanoString(self.gato)  + '\n Chaleco de alta visibilidad: ' + boleanoString(self.chaleco_alta_visibilidad)  + '\n Kit de bombillas' + boleanoString(self.kit_bombillas)  + '\n Kit de bombillas Fusibles' + boleanoString(self.kit_bombillas_fusibles)  + '\n Cod card: ' + boleanoString(self.cod_card)  + '\n Libre uso y mantenimiento' + boleanoString(self.libre_uso_mantenimiento)  + '\n Ficha técnia: ' + boleanoString(self.ficha_tecnica)  + '\n Permiso de circulación: ' + boleanoString(self.permiso_circulacion) + '\n ITV: ' + self.itv + '\n Fecha ITV: ' + self.fecha.strftime('%d/%m/%Y')
        return retornar

class Mantenimiento(models.Model):
    estado_revisiones = models.CharField(max_length=240, blank=True, null=True)
    mantenimiento_previo_entrega = models.CharField(max_length=240, blank=True, null=True)
    correa_servicio = models.CharField(max_length=240, blank=True, null=True)
    estado_bateria = models.CharField(max_length=240, blank=True, null=True)
    correa_distribucion = models.CharField(max_length=240, blank=True, null=True)
    ultimo_mantenimiento = models.CharField(max_length=240, blank=True, null=True)
    proximo_mantenimiento = models.CharField(max_length=240, blank=True, null=True)
    ultima_ITV = models.DateField()

    def __str__(self):
        retornar = 'Estado de revisiones: ' + self.estado_revisiones + '\n Mantenimiento previo Entrega: ' + self.mantenimiento_previo_entrega + '\n Correa de servicio: ' + self.correa_servicio + '\n Estado de la batería: ' + self.estado_bateria + '\n Correa de distribución: ' + self.correa_distribucion + '\n último Mantenimiento: ' + self.ultimo_mantenimiento + '\n Próximo Mantenimiento: ' + self.proximo_mantenimiento + '\n Última ITV: ' + self.ultima_ITV.strftime('%d/%m/%Y')
        return retornar

class ExamenVisual(models.Model):
    carroceria = models.CharField(max_length=240)
    descripcion_carroceria = models.CharField(max_length=240, blank=True, null=True)
    habitaculo_tapiceria_1 = models.CharField(max_length=240, blank=True, null=True)
    descripcion_habitaculo_tapiceria_1  = models.CharField(max_length=240, blank=True, null=True)
    habitaculo_tapiceria_2 = models.CharField(max_length=240, blank=True, null=True)
    descripcion_habitaculo_tapiceria_2  = models.CharField(max_length=240, blank=True, null=True)
    asiento_revestimiento_asiento = models.CharField(max_length=240, blank=True, null=True)
    descripcion_asiento_revestimiento_asiento = models.CharField(max_length=240, blank=True, null=True)
    neumaticos_delanteros = models.CharField(max_length=240, blank=True, null=True)
    descripcion_neumaticos_delanteros = models.CharField(max_length=240, blank=True, null=True)
    neumaticos_traseros = models.CharField(max_length=240, blank=True, null=True)
    descripcion_neumaticos_traseros = models.CharField(max_length=240, blank=True, null=True)
    volante_motor = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_volante_motor = models.TextField(blank=True, null=True)
    motor = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_motor = models.TextField(blank=True, null=True)
    sistema_escape = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_sistema_escape = models.TextField(blank=True, null=True)
    embrague = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_embrague = models.TextField(blank=True, null=True)
    alimentacion_inyeccion = models.CharField(max_length=240)
    explicacion_detallada_alimentacion_inyeccion = models.TextField(blank=True, null=True)
    cambio = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_cambio = models.TextField(blank=True, null=True)
    moto_arranque_alternador = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_moto_arranque_alternador = models.TextField(blank=True, null=True)
    diferencial_repartidor = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_diferencial_repartidor = models.TextField(blank=True, null=True)
    caja_transferencia = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_caja_transferencia = models.TextField(blank=True, null=True)
    organo_direccion = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_organo_direccion = models.TextField(blank=True, null=True)
    rodamiento_neumaticos = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_rodamiento_neumaticos = models.TextField(blank=True, null=True)
    direccion_asistida = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_direccion_asistida = models.TextField(blank=True, null=True)
    bomba_direccion_asistida = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_bomba_direccion_asistida = models.TextField(blank=True, null=True)
    sistema_frenado = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_sistema_frenado = models.TextField(blank=True, null=True)
    sistema_refrigeracion = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_sistema_refrigeracion = models.TextField(blank=True, null=True)
    sistema_calefaccion = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_sistema_calefaccion = models.TextField(blank=True, null=True)
    aire_acondicionado = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_aire_acondicionado = models.TextField(blank=True, null=True)
    abs_esp = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_abs_esp = models.TextField(blank=True, null=True)
    cuadro_instrumentos = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_cuadro_instrumentos = models.TextField(blank=True, null=True)
    limpiaparabrisas = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_limpiaparabrisas = models.TextField(blank=True, null=True)
    bomba_limpiaparabrisas = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_bomba_limpiaparabrisas = models.TextField(blank=True, null=True)
    sistema_electrico = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_sistema_electrico = models.TextField(blank=True, null=True)
    cierre_centralizado = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_cierre_centralizado = models.TextField(blank=True, null=True)
    alumbrado_señalizacion = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_alumbrado_señalizacion = models.TextField(blank=True, null=True)
    radio_lectorCD = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_radio_lectorCD = models.TextField(blank=True, null=True)
    navegador = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_navegador = models.TextField(blank=True, null=True)
    elevalunas_electrico = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_elevalunas_electrico = models.TextField(blank=True, null=True)
    airbag = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_airbag = models.TextField(blank=True, null=True)
    antirrobo = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_antirrobo = models.TextField(blank=True, null=True)
    techo_solar = models.CharField(max_length=240, blank=True, null=True)
    explicacion_detallada_techo_solar = models.TextField(blank=True, null=True)

    def __str__(self):
        retornar = 'Carrocería: ' + self.carroceria +'\n Descripción de Carrocería: ' + self.descripcion_carroceria + '\n' + '\n Habitáculo y Tapicería' + self.habitaculo_tapiceria_1 + '\n Descripción Habitáculo y tapicería 1: ' + self.descripcion_habitaculo_tapiceria_1 + '\n' + '\n Habitáculo y tapicería 2:' + self.habitaculo_tapiceria_2 + '\n Descripción Habitáculo y tapicería 2:' + self.descripcion_habitaculo_tapiceria_2 + '\n' + '\n Asiento y revestimiento del asiento' + self.asiento_revestimiento_asiento + '\n Descripción Asiento y revestimiento del asiento:' + self.descripcion_asiento_revestimiento_asiento + '\n' + '\n Neumáticos delanteros' + self.neumaticos_delanteros + '\n Descripción Neumáticos delanteros: ' + self.descripcion_neumaticos_delanteros + '\n' + '\n Neumáticos traseros' + self.neumaticos_traseros + '\n Descripción Neumáticos traseros: ' + self.descripcion_neumaticos_traseros + '\n' + '\n Volante motor:' + self.volante_motor + '\n Explicación detallada Volante motor: ' + self.explicacion_detallada_volante_motor + '\n' + '\n Motor:' + self.motor + '\n Explicación detallada Motor: ' + self.explicacion_detallada_motor + '\n' + '\n Sistema de escape:' + self.sistema_escape + '\n Explicación detallada Sistema de escape: ' + self.explicacion_detallada_sistema_escape + '\n' + '\n Embrague:' + self.embrague + '\n Explicación detallada Embrague: ' + self.explicacion_detallada_embrague + '\n' + '\n Alimentación e inyección:' + self.alimentacion_inyeccion + '\n Explicación detallada Alimentación e inyección: ' + self.explicacion_detallada_alimentacion_inyeccion + '\n' + '\n Cambio:' + self.cambio + '\n Explicación detallada Cambio: ' + self.explicacion_detallada_cambio + '\n' + '\n Motor de arranque/Alternador:' + self.moto_arranque_alternador + '\n Explicación detallada Motor de arranque/Alternador: ' + self.explicacion_detallada_moto_arranque_alternador + '\n'  + '\n Diferencial / Repartidor:' + self.diferencial_repartidor + '\n Explicación detallada Diferencial / Repartidor: ' + self.explicacion_detallada_diferencial_repartidor + '\n' + '\n Caja de trasferencia:' + self.caja_transferencia + '\n Explicación detallada Caja de trasferencia: ' + self.explicacion_detallada_caja_transferencia + '\n'  + '\n Organo de direccíon:' + self.organo_direccion + '\n Explicación detallada Organo de direccíon: ' + self.explicacion_detallada_organo_direccion + '\n' + '\n Rodamiento de los neumáticos:' + self.rodamiento_neumaticos + '\n Explicación detallada : Rodamiento de los neumáticos' + self.explicacion_detallada_rodamiento_neumaticos  + '\n' + '\n Dirección asistida:' + self.direccion_asistida + '\n Explicación detallada Dirección asistida: ' + self.explicacion_detallada_direccion_asistida + '\n' + '\n Bomba de la dirección asistida:' + self.bomba_direccion_asistida + '\n Explicación detallada Bomba de la dirección asistida: ' + self.explicacion_detallada_bomba_direccion_asistida  + '\n' + '\n Sistema de frenado:' + self.sistema_frenado + '\n Explicación detallada Sistema de frenado: ' + self.explicacion_detallada_sistema_frenado  + '\n' + '\n Sistema de refrigeración:' + self.sistema_refrigeracion + '\n Explicación detallada Sistema de refrigeración: ' + self.explicacion_detallada_sistema_refrigeracion  + '\n' + '\n Sistema de calefacción ( aire ):' + self.sistema_calefaccion + '\n Explicación detallada Sistema de calefacción ( aire ): ' + self.explicacion_detallada_sistema_calefaccion  + '\n'  + '\n Aire acondicionado:' + self.aire_acondicionado + '\n Explicación detallada Aire acondicionado: ' + self.explicacion_detallada_aire_acondicionado  + '\n'  + '\n ABS/ ESP:' + self.abs_esp + '\n Explicación detallada ABS/ ESP: ' + self.explicacion_detallada_abs_esp  + '\n' + '\n Cuadro de instrumentos:' + self.cuadro_instrumentos + '\n Explicación detallada Cuadro de instrumentos: ' + self.explicacion_detallada_cuadro_instrumentos + '\n' + '\n Limpiaparabrisas:' + self.limpiaparabrisas + '\n Explicación detallada Limpiaparabrisas: ' + self.explicacion_detallada_limpiaparabrisas  + '\n' + '\n Bomba limpiaparabrisas:' + self.bomba_limpiaparabrisas + '\n Explicación detallada Bomba limpiaparabrisas: ' + self.explicacion_detallada_bomba_limpiaparabrisas  + '\n' + '\n Sistema eléctrico:' + self.sistema_electrico + '\n Explicación detallada Sistema eléctrico: ' + self.explicacion_detallada_sistema_electrico  + '\n' + '\n Sistema Electrico:' + self.sistema_electrico + '\n Explicación detallada : ' + self.explicacion_detallada_sistema_electrico  + '\n' + '\n Cierre centralizado:' + self.cierre_centralizado + '\n Explicación detallada Cierre centralizado: ' + self.explicacion_detallada_cierre_centralizado  + '\n' + '\n Alumbrado y señalización:' + self.alumbrado_señalizacion + '\n Explicación detallada Alumbrado y señalización: ' + self.explicacion_detallada_alumbrado_señalizacion  + '\n' + '\n Radio / Lector CD:' + self.radio_lectorCD + '\n Explicación detallada Radio / Lector CD: ' + self.explicacion_detallada_radio_lectorCD  + '\n' + '\n Navegador:' + self.navegador + '\n Explicación detallada Navegador: ' + self.explicacion_detallada_navegador  + '\n' + '\n Elevalunas eléctrico:' + self.elevalunas_electrico + '\n Explicación detallada Elevalunas eléctrico: ' + self.explicacion_detallada_elevalunas_electrico  + '\n' + '\n Airbag:' + self.airbag + '\n Explicación detallada Airbag: ' + self.explicacion_detallada_airbag  + '\n' + '\n Antirrobo:' + self.antirrobo + '\n Explicación detallada Antirrobo: ' + self.explicacion_detallada_antirrobo  + '\n' + '\n Techo solar:' + self.techo_solar + '\n Explicación detallada Techo solar: ' + self.explicacion_detallada_techo_solar 
        return retornar

class Contrato(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contratoLocales = models.CharField(max_length=12, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    firmante = models.CharField(max_length=12, blank=True, null=True)
    nacido = models.CharField(max_length=12, blank=True, null=True)
    fechaNacimiento = models.DateField(blank=True, null=True)
    residenciaSede = models.CharField(max_length=12, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    profesion = models.CharField(max_length=12, blank=True, null=True)
    CifNif = models.CharField(max_length=12, blank=True, null=True)
    vendedor = models.CharField(max_length=12, blank=True, null=True)
    marca = models.CharField(max_length=12, blank=True, null=True)
    version = models.CharField(max_length=12, blank=True, null=True)
    modelo = models.CharField(max_length=12, blank=True, null=True)
    bastidor = models.CharField(max_length=12, blank=True, null=True)
    estadoEncontrado = models.CharField(max_length=12, blank=True, null=True)
    estadoEncontradoDescripcion = models.CharField(max_length=12, blank=True, null=True)
    marceEmpresa = models.CharField(max_length=12, blank=True, null=True)
    versionEmpresa = models.CharField(max_length=12, blank=True, null=True)
    modeloEmpresa = models.CharField(max_length=12, blank=True, null=True)
    bastidorEmpresa = models.CharField(max_length=12, blank=True, null=True)
    fechaPrimeraMatriculacion = models.DateField(blank=True, null=True)
    equivalenteAcordado = models.CharField(max_length=12, blank=True, null=True)
    equivalenteAcordadoMonto = models.CharField(max_length=12, blank=True, null=True)
    abonadoComprador = models.CharField(max_length=12, blank=True, null=True)
    abonadoCompradorMonto = models.CharField(max_length=12, blank=True, null=True)
    PrecioAcordado = models.CharField(max_length=12, blank=True, null=True)
    valorVehiculoRetirado = models.CharField(max_length=12, blank=True, null=True)
    depostoGarantiaPagado = models.CharField(max_length=12, blank=True, null=True)
    sociedadFinanciera = models.CharField(max_length=12, blank=True, null=True)
    nroProtocolo = models.CharField(max_length=12, blank=True, null=True)
    importaFinanciado = models.CharField(max_length=12, blank=True, null=True)
    gastosInstruccionSello = models.CharField(max_length=12, blank=True, null=True)
    nroPlazos = models.CharField(max_length=12, blank=True, null=True)
    importePlazos = models.CharField(max_length=12, blank=True, null=True)
    lugar = models.CharField(max_length=12, blank=True, null=True)
    fecha2 = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

class Insercion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    concesionario = models.CharField(max_length=240, blank=True, null=True)
    insercion_de_Vehiculo = models.CharField(max_length=240, blank=True, null=True)
    datos_del_Vehiculo = models.OneToOneField(DatosVehiculo, on_delete=models.CASCADE, blank=True, null=True)
    suplementos = models.OneToOneField(Suplemento, on_delete=models.CASCADE, blank=True, null=True)
    datos_del_comprador = models.OneToOneField(DatosComprador, on_delete=models.CASCADE, blank=True, null=True)
    duracion_del_contrato = models.CharField(max_length=240, blank=True, null=True)
    documentacion = models.OneToOneField(Documentacion, on_delete=models.CASCADE, blank=True, null=True)
    mantenimiento = models.OneToOneField(Mantenimiento, on_delete=models.CASCADE, blank=True, null=True)
    examen_visual = models.OneToOneField(ExamenVisual, on_delete=models.CASCADE, blank=True, null=True)
    contrato = models.OneToOneField(Contrato, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.concesionario

    class Meta:
        verbose_name = "Inserción"
        verbose_name_plural = "Inserciones"



