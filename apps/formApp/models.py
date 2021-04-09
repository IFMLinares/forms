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

    class Meta:
        db_table = 'auth_user'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class DatosVehiculo(models.Model):
    matricula = models.CharField(max_length=240)
    marca = models.CharField(max_length=240)
    modelo = models.CharField(max_length=240)
    alimentacion = models.CharField(max_length=240)
    clase_de_cont = models.CharField(max_length=240) #clase de control
    prime_matr  = models.CharField(max_length=240) #primera matricula
    version = models.CharField(max_length=240)
    bastidor = models.CharField(max_length=240)
    potencia_KW = models.CharField(max_length=240)
    nro_propietarios_Privados  = models.CharField(max_length=240)
    nro_propietarios_profesionales = models.CharField(max_length=240)
    cilindrada = models.CharField(max_length=240)
    color = models.CharField(max_length=240)
    fecha_entrega = models.DateField()
    fecha_inicio = models.DateField()
    fecha_activacion = models.DateField()

    def __str__(self):
        retornar = 'Matricula ' + self.matricula + '\n Marca: ' + self.marca + '\n Modelo: ' + self.modelo + '\n Alimentacion: ' + self.alimentacion + '\n clase de cont: ' + self.clase_de_cont + '\n Primer matricula: ' + self.prime_matr + '\n potencia_KW: ' + self.potencia_KW + '\n nro propietarios Privados: ' + self.nro_propietarios_Privados + '\n nro propietarios profesionales: ' + self.nro_propietarios_profesionales + '\n cilindrada: ' + self.cilindrada + '\n color: ' + self.color + '\n fecha_entrega: ' + self.fecha_entrega.strftime('%d/%m/%Y') + '\n fecha_inicio: ' + self.fecha_inicio.strftime('%d/%m/%Y') + '\n fecha_activacion: ' + self.fecha_activacion.strftime('%d/%m/%Y')
        return retornar

    class Meta:
        verbose_name = "Datos del vehiculo"
        verbose_name_plural = "Datos de los vehiculos"

class Suplemento(models.Model):
    cuatro_por_cuatro = models.BooleanField()
    super_Car = models.BooleanField()
    cambio_autom = models.BooleanField()
    suv = models.BooleanField()
    vehiculo_comercial = models.BooleanField()
    cobertura = models.BooleanField()

    def __str__(self):
        retornar = '4x4: ' + boleanoString(self.cuatro_por_cuatro) + '\n Super car: ' + boleanoString(self.super_Car) + '\n Cambio automatico: ' + boleanoString(self.cambio_autom) + '\n Suv: ' + boleanoString(self.suv) + '\n Vehículo comercial: ' + boleanoString(self.vehiculo_comercial) + '\n +Cobertura: ' + boleanoString(self.cobertura)
        return retornar

class DatosComprador(models.Model):
    nombre_Completo = models.CharField(max_length=240)
    codigo_postal = models.CharField(max_length=240)
    localidad_Provincia_Pais = models.CharField(max_length=240)
    email = models.EmailField()
    direccion = models.CharField(max_length=240)
    numero_de_telefono  = models.CharField(max_length=240)
    numero_de_movil = models.CharField(max_length=240)
    documento_identidad = models.CharField(max_length=240)

    def __str__(self):
        retornar = 'Nombre completo: ' + self.nombre_Completo + '\n Código Postal: ' +  self.codigo_postal + '\n Localidad/Provincia/País: ' + self.localidad_Provincia_Pais + '\n Email: ' + self.email + '\n Dirección: ' + self.direccion + '\n Número de telefono: ' + self.numero_de_telefono + '\n Número Móvil: ' + self.numero_de_movil + '\n Documento de Identidad: ' + self.documento_identidad
        return retornar

class Documentacion(models.Model):
    rueda_repuesto1 = models.BooleanField()
    rueda_repuesto2 = models.BooleanField()
    duplicado_llaves = models.BooleanField()
    kit_inflado = models.BooleanField()
    triangulo_emergencia = models.BooleanField()
    gato = models.BooleanField()
    chaleco_alta_visibilidad = models.BooleanField()
    kit_bombillas = models.BooleanField()
    kit_bombillas_fusibles = models.BooleanField()
    cod_card = models.BooleanField()
    libre_uso_mantenimiento = models.BooleanField()
    ficha_tecnica = models.BooleanField()
    permiso_circulacion = models.BooleanField()

    itv = models.CharField(max_length=240)
    fecha = models.DateField()

    def __str__(self):
        retornar = 'Rueda de Repuesto 1: ' + boleanoString(self.rueda_repuesto1) + '\n Rueda de Repuesto 2: ' + boleanoString(self.rueda_repuesto2) + '\n Kit de Inflado: ' + boleanoString(self.kit_inflado) + '\n Triángulo de emergencia: ' + boleanoString(self.triangulo_emergencia)  + '\n Gato: ' + boleanoString(self.gato)  + '\n Chaleco de alta visibilidad: ' + boleanoString(self.chaleco_alta_visibilidad)  + '\n Kit de bombillas' + boleanoString(self.kit_bombillas)  + '\n Kit de bombillas Fusibles' + boleanoString(self.kit_bombillas_fusibles)  + '\n Cod card: ' + boleanoString(self.cod_card)  + '\n Libre uso y mantenimiento' + boleanoString(self.libre_uso_mantenimiento)  + '\n Ficha técnia: ' + boleanoString(self.ficha_tecnica)  + '\n Permiso de circulación: ' + boleanoString(self.permiso_circulacion) 
        return retornar

class Mantenimiento(models.Model):
    estado_revisiones = models.CharField(max_length=240)
    mantenimiento_previo_entrega = models.CharField(max_length=240)
    correa_servicio = models.CharField(max_length=240)
    estado_bateria = models.CharField(max_length=240)
    correa_distribucion = models.CharField(max_length=240)
    ultimo_mantenimiento = models.CharField(max_length=240)
    proximo_mantenimiento = models.CharField(max_length=240)
    ultima_ITV = models.DateField()

    def __str__(self):
        retornar = 'Estado de revisiones: ' + boleanoString(self.estado_revisiones) + '\n Mantenimiento: ' + boleanoString(self.mantenimiento_previo_entrega) + '\n Correa de servicio: ' + boleanoString(self.correa_servicio) + '\n Estado de la batería' + boleanoString(self.estado_bateria) + '\n Correa de distribución' + boleanoString(self.correa_distribucion) + '\n último Mantenimiento' + boleanoString(self.ultimo_mantenimiento) + '\n Próximo Mantenimiento' + boleanoString(self.proximo_mantenimiento) + '\n Última ITV' + boleanoString(self.ultima_ITV)
        return retornar

class ExamenVisual(models.Model):
    carroceria = models.CharField(max_length=240)
    descripcion_carroceria = models.CharField(max_length=240)
    habitaculo_tapiceria_1 = models.CharField(max_length=240)
    descripcion_habitaculo_tapiceria_1  = models.CharField(max_length=240)
    habitaculo_tapiceria_2 = models.CharField(max_length=240)
    descripcion_habitaculo_tapiceria_2  = models.CharField(max_length=240)
    asiento_revestimiento_asiento = models.CharField(max_length=240)
    descripcion_asiento_revestimiento_asiento = models.CharField(max_length=240)
    neumaticos_delanteros = models.CharField(max_length=240)
    descripcion_neumaticos_delanteros = models.CharField(max_length=240)
    neumaticos_traseros = models.CharField(max_length=240)
    descripcion_neumaticos_traseros = models.CharField(max_length=240)
    volante_motor = models.CharField(max_length=240)
    explicacion_detallada_volante_motor = models.TextField()
    motor = models.CharField(max_length=240)
    explicacion_detallada_motor = models.TextField()
    sistema_escape = models.CharField(max_length=240)
    explicacion_detallada_sistema_escape = models.TextField()
    embrague = models.CharField(max_length=240)
    explicacion_detallada_embrague = models.TextField()
    alimentacion_inyeccion = models.CharField(max_length=240)
    explicacion_detallada_alimentacion_inyeccion = models.TextField()
    cambio = models.CharField(max_length=240)
    explicacion_detallada_cambio = models.TextField()
    moto_arranque_alternador = models.CharField(max_length=240)
    explicacion_detallada_moto_arranque_alternador = models.TextField()
    diferencial_repartidor = models.CharField(max_length=240)
    explicacion_detallada_diferencial_repartidor = models.TextField()
    caja_transferencia = models.CharField(max_length=240)
    explicacion_detallada_caja_transferencia = models.TextField()
    organo_direccion = models.CharField(max_length=240)
    explicacion_detallada_organo_direccion = models.TextField()
    rodamiento_neumaticos = models.CharField(max_length=240)
    explicacion_detallada_rodamiento_neumaticos = models.TextField()
    direccion_asistida = models.CharField(max_length=240)
    explicacion_detallada_direccion_asistida = models.TextField()
    bomba_direccion_asistida = models.CharField(max_length=240)
    explicacion_detallada_bomba_direccion_asistida = models.TextField()
    sistema_frenado = models.CharField(max_length=240)
    explicacion_detallada_sistema_frenado = models.TextField()
    sistema_refrigeracion = models.CharField(max_length=240)
    explicacion_detallada_sistema_refrigeracion = models.TextField()
    sistema_calefaccion = models.CharField(max_length=240)
    explicacion_detallada_sistema_calefaccion = models.TextField()
    aire_acondicionado = models.CharField(max_length=240)
    explicacion_detallada_aire_acondicionado = models.TextField()
    abs_esp = models.CharField(max_length=240)
    explicacion_detallada_abs_esp = models.TextField()
    cuadro_instrumentos = models.CharField(max_length=240)
    explicacion_detallada_cuadro_instrumentos = models.TextField()
    limpiaparabrisas = models.CharField(max_length=240)
    explicacion_detallada_limpiaparabrisas = models.TextField()
    bomba_limpiaparabrisas = models.CharField(max_length=240)
    explicacion_detallada_bomba_limpiaparabrisas = models.TextField()
    sistema_electrico = models.CharField(max_length=240)
    explicacion_detallada_sistema_electrico = models.TextField()
    cierre_centralizado = models.CharField(max_length=240)
    explicacion_detallada_cierre_centralizado = models.TextField()
    alumbrado_señalizacion = models.CharField(max_length=240)
    explicacion_detallada_alumbrado_señalizacion = models.TextField()
    radio_lectorCD = models.CharField(max_length=240)
    explicacion_detallada_radio_lectorCD = models.TextField()
    navegador = models.CharField(max_length=240)
    explicacion_detallada_navegador = models.TextField()
    elevalunas_electrico = models.CharField(max_length=240)
    explicacion_detallada_elevalunas_electrico = models.TextField()
    airbag = models.CharField(max_length=240)
    explicacion_detallada_airbag = models.TextField()
    antirrobo = models.CharField(max_length=240)
    explicacion_detallada_antirrobo = models.TextField()
    techo_solar = models.CharField(max_length=240)
    explicacion_detallada_techo_solar = models.TextField()

    def __str__(self):
        retornar = 'Carrocería: ' + self.carroceria +'\n Descripción de Carrocería: ' + self.descripcion_carroceria + '\n' + '\n Habitáculo y Tapicería' + self.habitaculo_tapiceria_1 + '\n Descripción Habitáculo y tapicería 1: ' + self.descripcion_habitaculo_tapiceria_1 + '\n' + '\n Habitáculo y tapicería 2:' + self.habitaculo_tapiceria_2 + '\n Descripción Habitáculo y tapicería 2:' + self.descripcion_habitaculo_tapiceria_2 + '\n' + '\n Asiento y revestimiento del asiento' + self.asiento_revestimiento_asiento + '\n Descripción Asiento y revestimiento del asiento:' + self.descripcion_asiento_revestimiento_asiento + '\n' + '\n Neumáticos delanteros' + self.neumaticos_delanteros + '\n Descripción Neumáticos delanteros: ' + self.descripcion_neumaticos_delanteros + '\n' + '\n Neumáticos traseros' + self.neumaticos_traseros + '\n Descripción Neumáticos traseros: ' + self.descripcion_neumaticos_traseros + '\n' + '\n Volante motor:' + self.volante_motor + '\n Explicación detallada Volante motor: ' + self.explicacion_detallada_volante_motor + '\n' + '\n Motor:' + self.motor + '\n Explicación detallada Motor: ' + self.explicacion_detallada_motor + '\n' + '\n Sistema de escape:' + self.sistema_escape + '\n Explicación detallada Sistema de escape: ' + self.explicacion_detallada_sistema_escape + '\n' + '\n Embrague:' + self.embrague + '\n Explicación detallada Embrague: ' + self.explicacion_detallada_embrague + '\n' + '\n Alimentación e inyección:' + self.alimentacion_inyeccion + '\n Explicación detallada Alimentación e inyección: ' + self.explicacion_detallada_alimentacion_inyeccion + '\n' + '\n Cambio:' + self.cambio + '\n Explicación detallada Cambio: ' + self.explicacion_detallada_cambio + '\n' + '\n Motor de arranque/Alternador:' + self.moto_arranque_alternador + '\n Explicación detallada Motor de arranque/Alternador: ' + self.explicacion_detallada_moto_arranque_alternador + '\n'  + '\n Diferencial / Repartidor:' + self.diferencial_repartidor + '\n Explicación detallada Diferencial / Repartidor: ' + self.explicacion_detallada_diferencial_repartidor + '\n' + '\n Caja de trasferencia:' + self.caja_transferencia + '\n Explicación detallada Caja de trasferencia: ' + self.explicacion_detallada_caja_transferencia + '\n'  + '\n Organo de direccíon:' + self.organo_direccion + '\n Explicación detallada Organo de direccíon: ' + self.explicacion_detallada_organo_direccion + '\n' + '\n Rodamiento de los neumáticos:' + self.rodamiento_neumaticos + '\n Explicación detallada : Rodamiento de los neumáticos' + self.explicacion_detallada_rodamiento_neumaticos  + '\n' + '\n Dirección asistida:' + self.direccion_asistida + '\n Explicación detallada Dirección asistida: ' + self.explicacion_detallada_direccion_asistida + '\n' + '\n Bomba de la dirección asistida:' + self.bomba_direccion_asistida + '\n Explicación detallada Bomba de la dirección asistida: ' + self.explicacion_detallada_bomba_direccion_asistida  + '\n' + '\n Sistema de frenado:' + self.sistema_frenado + '\n Explicación detallada Sistema de frenado: ' + self.explicacion_detallada_sistema_frenado  + '\n' + '\n Sistema de refrigeración:' + self.sistema_refrigeracion + '\n Explicación detallada Sistema de refrigeración: ' + self.explicacion_detallada_sistema_refrigeracion  + '\n' + '\n Sistema de calefacción ( aire ):' + self.sistema_calefaccion + '\n Explicación detallada Sistema de calefacción ( aire ): ' + self.explicacion_detallada_sistema_calefaccion  + '\n'  + '\n Aire acondicionado:' + self.aire_acondicionado + '\n Explicación detallada Aire acondicionado: ' + self.explicacion_detallada_aire_acondicionado  + '\n'  + '\n ABS/ ESP:' + self.abs_esp + '\n Explicación detallada ABS/ ESP: ' + self.explicacion_detallada_abs_esp  + '\n' + '\n Cuadro de instrumentos:' + self.cuadro_instrumentos + '\n Explicación detallada Cuadro de instrumentos: ' + self.explicacion_detallada_cuadro_instrumentos + '\n' + '\n Limpiaparabrisas:' + self.limpiaparabrisas + '\n Explicación detallada Limpiaparabrisas: ' + self.explicacion_detallada_limpiaparabrisas  + '\n' + '\n Bomba limpiaparabrisas:' + self.bomba_limpiaparabrisas + '\n Explicación detallada Bomba limpiaparabrisas: ' + self.explicacion_detallada_bomba_limpiaparabrisas  + '\n' + '\n Sistema eléctrico:' + self.sistema_electrico + '\n Explicación detallada Sistema eléctrico: ' + self.explicacion_detallada_sistema_electrico  + '\n' + '\n Sistema Electrico:' + self.sistema_electrico + '\n Explicación detallada : ' + self.explicacion_detallada_sistema_electrico  + '\n' + '\n Cierre centralizado:' + self.cierre_centralizado + '\n Explicación detallada Cierre centralizado: ' + self.explicacion_detallada_cierre_centralizado  + '\n' + '\n Alumbrado y señalización:' + self.alumbrado_señalizacion + '\n Explicación detallada Alumbrado y señalización: ' + self.explicacion_detallada_alumbrado_señalizacion  + '\n' + '\n Radio / Lector CD:' + self.radio_lectorCD + '\n Explicación detallada Radio / Lector CD: ' + self.explicacion_detallada_radio_lectorCD  + '\n' + '\n Navegador:' + self.navegador + '\n Explicación detallada Navegador: ' + self.explicacion_detallada_navegador  + '\n' + '\n Elevalunas eléctrico:' + self.elevalunas_electrico + '\n Explicación detallada Elevalunas eléctrico: ' + self.explicacion_detallada_elevalunas_electrico  + '\n' + '\n Airbag:' + self.airbag + '\n Explicación detallada Airbag: ' + self.explicacion_detallada_airbag  + '\n' + '\n Antirrobo:' + self.antirrobo + '\n Explicación detallada Antirrobo: ' + self.explicacion_detallada_antirrobo  + '\n' + '\n Techo solar:' + self.techo_solar + '\n Explicación detallada Techo solar: ' + self.explicacion_detallada_techo_solar 
        return retornar

class Contrato(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contratoLocales = models.CharField(max_length=12)
    fecha = models.DateField()
    firmante = models.CharField(max_length=12)
    nacido = models.CharField(max_length=12)
    fechaNacimiento = models.DateField()
    residenciaSede = models.CharField(max_length=12)
    telefono = models.CharField(max_length=12)
    profesion = models.CharField(max_length=12)
    CifNif = models.CharField(max_length=12)
    vendedor = models.CharField(max_length=12)
    marca = models.CharField(max_length=12)
    version = models.CharField(max_length=12)
    modelo = models.CharField(max_length=12)
    bastidor = models.CharField(max_length=12)
    estadoEncontrado = models.CharField(max_length=12)
    estadoEncontradoDescripcion = models.CharField(max_length=12)
    marceEmpresa = models.CharField(max_length=12)
    versionEmpresa = models.CharField(max_length=12)
    modeloEmpresa = models.CharField(max_length=12)
    bastidorEmpresa = models.CharField(max_length=12)
    fechaPrimeraMatriculacion = models.DateField()
    equivalenteAcordado = models.CharField(max_length=12)
    equivalenteAcordadoMonto = models.CharField(max_length=12)
    abonadoComprador = models.CharField(max_length=12)
    abonadoCompradorMonto = models.CharField(max_length=12)
    PrecioAcordado = models.CharField(max_length=12)
    valorVehiculoRetirado = models.CharField(max_length=12)
    depostoGarantiaPagado = models.CharField(max_length=12)
    sociedadFinanciera = models.CharField(max_length=12)
    nroProtocolo = models.CharField(max_length=12)
    importaFinanciado = models.CharField(max_length=12)
    gastosInstruccionSello = models.CharField(max_length=12)
    nroPlazos = models.CharField(max_length=12)
    importePlazos = models.CharField(max_length=12)
    lugar = models.CharField(max_length=12)
    fecha2 = models.DateField()
    total = models.FloatField()

class Insercion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    concesionario = models.CharField(max_length=240)
    insercion_de_Vehiculo = models.CharField(max_length=240)
    datos_del_Vehiculo = models.OneToOneField(DatosVehiculo, on_delete=models.CASCADE)
    suplementos = models.OneToOneField(Suplemento, on_delete=models.CASCADE)
    datos_del_comprador = models.OneToOneField(DatosComprador, on_delete=models.CASCADE)
    duracion_del_contrato = models.CharField(max_length=240)
    documentacion = models.OneToOneField(Documentacion, on_delete=models.CASCADE)
    mantenimiento = models.OneToOneField(Mantenimiento, on_delete=models.CASCADE)
    examen_visual = models.OneToOneField(ExamenVisual, on_delete=models.CASCADE)
    contrato = models.OneToOneField(Contrato, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.concesionario



