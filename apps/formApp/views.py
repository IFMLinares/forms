import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View, DetailView, ListView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    Insercion,
    DatosVehiculo,
    Suplemento,
    DatosComprador,
    Documentacion,
    Mantenimiento,
    ExamenVisual,
    Contrato,
    User
)

# Create your views here.



# Vista de insercion de vehiculos
class FormInsercionView(LoginRequiredMixin, TemplateView):
    template_name = 'insercion.html'


    def post(self, *args, **kwargs):
        # POLITICAS Y PRIVACIDAD:
        concesionario = self.request.POST['concesionario']

        # INSERCION DE VEHICULOS
        nombreComercial = self.request.POST['nombreComercial']

        # DATOS DEL VEHICULO
        matricula = self.request.POST['matricula']
        transmision = self.request.POST['transmision']
        marca = self.request.POST['marca']
        modelo = self.request.POST['modelo']
        alimentacion = self.request.POST['alimentacion']
        claseControl = self.request.POST['claseControl']
        primeraMatricula = self.request.POST['primeraMatricula']
        version = self.request.POST['version']
        potenciaKW = self.request.POST['potenciaKW']
        nroPropietariosPrivados = self.request.POST['nroPropietariosPrivados']
        nroPropietariosProfesionales = self.request.POST['nroPropietariosProfesionales']
        cilindrada = self.request.POST['cilindrada']
        bastidor = self.request.POST['bastidor']
        color = self.request.POST['color']
        fechaEntrega = self.request.POST['fechaEntrega']
        fechaInicio = self.request.POST['fechaInicio']
        fechaActivacion = self.request.POST['fechaActivacion']

        # suplementos
        cuatroxcuatro = self.request.POST['cuatroxcuatro']
        cambioautomatico = self.request.POST['cambioautomatico']
        vehiculoComercial = self.request.POST['vehiculoComercial']
        superCar = self.request.POST['superCar']
        suv = self.request.POST['suv']
        cobertura = self.request.POST['cobertura']

        # DATOS DEL COMPRADOR
        nombreCompleto = self.request.POST['nombreCompleto']
        direccion = self.request.POST['direccion']
        codigoPostal = self.request.POST['codigoPostal']
        numeroTelefono = self.request.POST['numeroTelefono']
        localidad = self.request.POST['localidad']
        numeroMovil = self.request.POST['numeroMovil']
        email = self.request.POST['email']
        documentoIdentidad = self.request.POST['documentoIdentidad']

        # DURACION DEL CONTRATO
        duracionContrato = self.request.POST['duracionContrato']

        # DOCUMENTACION:
        try:
            ruedaRepuesto1 = self.request.POST['ruedaRepuesto1']
        except:
            ruedaRepuesto1 = 0
        try:
            kitInflado = self.request.POST['kitInflado']
        except:
            kitInflado = 0
        try:
            trianguloEmergencia = self.request.POST['trianguloEmergencia']
        except:
            trianguloEmergencia = 0
        try:
            gato = self.request.POST['gato']
        except:
            gato = 0
        try:
            chalecoAltaVelocidad = self.request.POST['chalecoAltaVelocidad']
        except:
            chalecoAltaVelocidad = 0
        try:
            kitBombillas = self.request.POST['kitBombillas']
        except:
            kitBombillas = 0
        try:
            kitBombillasFusibles = self.request.POST['kitBombillasFusibles']
        except:
            kitBombillasFusibles = 0
        try:
            duplicadoLlaves = self.request.POST['duplicadoLlaves']
        except:
            duplicadoLlaves = 0
        try:
            codCard = self.request.POST['codCard']
        except:
            codCard = 0
        try:
            libreUsoMantenimiento = self.request.POST['libreUsoMantenimiento'] = 0
        except:
            libreUsoMantenimiento = 0
        try:
            fichaTecnica = self.request.POST['fichaTecnica']
        except:
            fichaTecnica= 0
        try:
            permisoCirculacion = self.request.POST['permisoCirculacion']
        except:
            permisoCirculacion= 0
        try:
            fechaITV = self.request.POST['fechaITV']
        except:
            fechaITV = 0
        itv = self.request.POST['itv']

        # MANTENIMIENTO:
        estadoRevisiones = self.request.POST['estadoRevisiones']
        mantenimientoPrevioEntrega = self.request.POST['mantenimientoPrevioEntrega']
        correaServicio = self.request.POST['correaServicio']
        estadoBateria = self.request.POST['estadoBateria']
        correaDistribucion = self.request.POST['correaDistribucion']
        ultimoMantenimiento = self.request.POST['ultimoMantenimiento']
        proximoMantenimiento = self.request.POST['proximoMantenimiento']
        ultimaITV = self.request.POST['ultimaITV']

        # EXAMEN VISUAL:
        carroceria = self.request.POST['carroceria']
        descripcionCarroceria = self.request.POST['descripcionCarroceria']
        habitaculoTapiceria = self.request.POST['habitaculoTapiceria']
        descripcionHabitaculoTapiceria = self.request.POST['descripcionHabitaculoTapiceria']
        habitaculoTapiceria2 = self.request.POST['habitaculoTapiceria2']
        descripcionHabitaculoTapiceria2 = self.request.POST['descripcionHabitaculoTapiceria2']
        asientoRevestimientoAsiento = self.request.POST['asientoRevestimientoAsiento']
        descripcionAsientoRevestimientoAsiento = self.request.POST['descripcionAsientoRevestimientoAsiento']
        neumaticosDelanteros = self.request.POST['neumaticosDelanteros']
        descripcionNeumaticosDelanteros = self.request.POST['descripcionNeumaticosDelanteros']
        neumaticosTraseros = self.request.POST['neumaticosTraseros']
        descripcionNeumaticosTraseros = self.request.POST['descripcionNeumaticosTraseros']
        volanteMotor = self.request.POST['volanteMotor']
        descripcionVolanteMotor = self.request.POST['descripcionVolanteMotor']
        motor = self.request.POST['motor']
        Explicacionmotor = self.request.POST['Explicacionmotor']
        sistemaEscape = self.request.POST['sistemaEscape']
        explicacionsistemaEscape = self.request.POST['explicacionsistemaEscape']
        embrague = self.request.POST['embrague']
        descripcionEmbrague = self.request.POST['descripcionEmbrague']
        alimentacionInyeccion = self.request.POST['alimentacionInyeccion']
        explicacionAlimentacionInyeccion = self.request.POST['explicacionAlimentacionInyeccion']
        cambio = self.request.POST['cambio']
        explicacionCambio = self.request.POST['explicacionCambio']
        motorArranqueAlternador = self.request.POST['motorArranqueAlternador']
        explicacionMotorArranqueAlternador = self.request.POST['explicacionMotorArranqueAlternador']
        diferencialRepartidor = self.request.POST['diferencialRepartidor']
        explicacionDiferencialRepartidor = self.request.POST['explicacionDiferencialRepartidor']
        cajaTranferencia = self.request.POST['cajaTranferencia']
        explicacionCajaTranferencia = self.request.POST['explicacionCajaTranferencia']
        organoDireccion = self.request.POST['organoDireccion']
        explicacionOrganoDireccion = self.request.POST['explicacionOrganoDireccion']
        rodamientoNeumaticos = self.request.POST['rodamientoNeumaticos']
        ExplicacionRodamientoNeumaticos = self.request.POST['ExplicacionRodamientoNeumaticos']
        direccionAsistida = self.request.POST['direccionAsistida']
        explicacionDireccionAsistida = self.request.POST['explicacionDireccionAsistida']
        bombaDireccionAsistida = self.request.POST['bombaDireccionAsistida']
        explicacionbombaDireccionAsistida = self.request.POST['explicacionbombaDireccionAsistida']
        sistemaFrenado = self.request.POST['sistemaFrenado']
        explicacionSistemaFrenado = self.request.POST['explicacionSistemaFrenado']
        sistemaRefrigeracion = self.request.POST['sistemaRefrigeracion']
        explicacionSistemaRefrigeracion = self.request.POST['explicacionSistemaRefrigeracion']
        sistemaCalefaccion = self.request.POST['sistemaCalefaccion']
        explicacionSistemaCalefaccion = self.request.POST['explicacionSistemaCalefaccion']
        aireAcondicionado = self.request.POST['aireAcondicionado']
        expliacionAireAcondicionado = self.request.POST['expliacionAireAcondicionado']
        AbsEsp = self.request.POST['AbsEsp']
        explicacionAbsEsp = self.request.POST['explicacionAbsEsp']
        cuadroInstrumentos = self.request.POST['cuadroInstrumentos']
        explicacionCuadroInstrumentos = self.request.POST['explicacionCuadroInstrumentos']
        limpiaParabrisas = self.request.POST['limpiaParabrisas']
        explicacionLimpiaParabrisas = self.request.POST['explicacionLimpiaParabrisas']
        bombaLimpiaparabrisas = self.request.POST['bombaLimpiaparabrisas']
        explicacionbombaLimpiaparabrisas = self.request.POST['explicacionbombaLimpiaparabrisas']
        sistemaElectrico = self.request.POST['sistemaElectrico']
        explicacionSistemaElectrico = self.request.POST['explicacionSistemaElectrico']
        cierreCentralizado = self.request.POST['cierreCentralizado']
        expliacionCierreCentralizado = self.request.POST['expliacionCierreCentralizado']
        alumbradoSeñalizacion = self.request.POST['alumbradoSeñalizacion']
        expliacionAlumbradoSeñalizacion = self.request.POST['expliacionAlumbradoSeñalizacion']
        radioLector = self.request.POST['radioLector']
        explicacionRadioLector = self.request.POST['explicacionRadioLector']
        navegador = self.request.POST['navegador']
        explicacionNavegador = self.request.POST['explicacionNavegador']
        elevalunasElectrico = self.request.POST['elevalunasElectrico']
        explicacionElevalunasElectrico = self.request.POST['explicacionElevalunasElectrico']
        airBag = self.request.POST['airBag']
        explicacionAirBag = self.request.POST['explicacionAirBag']
        antirrobo = self.request.POST['antirrobo']
        explicacionAntirrobo = self.request.POST['explicacionAntirrobo']
        techoSolar = self.request.POST['techoSolar']
        expliacionTechoSolar = self.request.POST['expliacionTechoSolar']

        datosVehiculo = DatosVehiculo(
            matricula=matricula,
            transmision=transmision,
            marca=marca,
            modelo=modelo,
            version=version,
            bastidor=bastidor,
            alimentacion=alimentacion,
            clase_de_cont=claseControl,
            prime_matr=primeraMatricula,
            potencia_KW=potenciaKW,
            nro_propietarios_Privados=nroPropietariosPrivados,
            nro_propietarios_profesionales=nroPropietariosProfesionales,
            cilindrada=cilindrada,
            color=color,
            fecha_entrega=fechaEntrega,
            fecha_inicio=fechaInicio,
            fecha_activacion=fechaActivacion
        )

        suplementos = Suplemento(
            cuatro_por_cuatro=cuatroxcuatro,
            super_Car=superCar,
            cambio_autom=cambioautomatico,
            suv=suv,
            vehiculo_comercial=vehiculoComercial,
            cobertura=cobertura
        )

        datosDelComprador = DatosComprador(
            nombre_Completo=nombreCompleto,
            codigo_postal=codigoPostal,
            localidad_Provincia_Pais=localidad,
            email=email,
            direccion=direccion,
            numero_de_telefono=numeroTelefono,
            numero_de_movil=numeroMovil,
            documento_identidad=documentoIdentidad
        )

        documentacion = Documentacion(
            rueda_repuesto1=ruedaRepuesto1,
            duplicado_llaves=duplicadoLlaves,
            kit_inflado=kitInflado,
            triangulo_emergencia=trianguloEmergencia,
            gato=gato,
            chaleco_alta_visibilidad=chalecoAltaVelocidad,
            kit_bombillas=kitBombillas,
            kit_bombillas_fusibles=kitBombillasFusibles,
            cod_card=codCard,
            libre_uso_mantenimiento=libreUsoMantenimiento,
            ficha_tecnica=fichaTecnica,
            permiso_circulacion=permisoCirculacion,
            itv=itv,
            fecha=fechaITV,
        )

        mantenimiento = Mantenimiento(
            estado_revisiones=estadoRevisiones,
            mantenimiento_previo_entrega=mantenimientoPrevioEntrega,
            correa_servicio=correaServicio,
            estado_bateria=estadoBateria,
            correa_distribucion=correaDistribucion,
            ultimo_mantenimiento=ultimoMantenimiento,
            proximo_mantenimiento=proximoMantenimiento,
            ultima_ITV=ultimaITV
        )

        examenVisual = ExamenVisual(
            carroceria=carroceria,
            descripcion_carroceria=descripcionCarroceria,
            habitaculo_tapiceria_1=habitaculoTapiceria,
            descripcion_habitaculo_tapiceria_1=descripcionHabitaculoTapiceria,
            habitaculo_tapiceria_2=habitaculoTapiceria2,
            descripcion_habitaculo_tapiceria_2=descripcionHabitaculoTapiceria2,
            asiento_revestimiento_asiento=asientoRevestimientoAsiento,
            descripcion_asiento_revestimiento_asiento=descripcionAsientoRevestimientoAsiento,
            neumaticos_delanteros=neumaticosDelanteros,
            descripcion_neumaticos_delanteros=descripcionNeumaticosDelanteros,
            neumaticos_traseros=neumaticosTraseros,
            descripcion_neumaticos_traseros=descripcionNeumaticosTraseros,
            volante_motor=volanteMotor,
            explicacion_detallada_volante_motor=descripcionVolanteMotor,
            motor=motor,
            explicacion_detallada_motor=Explicacionmotor,
            sistema_escape=sistemaEscape,
            explicacion_detallada_sistema_escape=explicacionsistemaEscape,
            embrague=embrague,
            explicacion_detallada_embrague=descripcionEmbrague,
            alimentacion_inyeccion=alimentacionInyeccion,
            explicacion_detallada_alimentacion_inyeccion=explicacionAlimentacionInyeccion,
            cambio=cambio,
            explicacion_detallada_cambio=explicacionCambio,
            moto_arranque_alternador=motorArranqueAlternador,
            explicacion_detallada_moto_arranque_alternador=explicacionMotorArranqueAlternador,
            diferencial_repartidor=diferencialRepartidor,
            explicacion_detallada_diferencial_repartidor=explicacionDiferencialRepartidor,
            caja_transferencia=cajaTranferencia,
            explicacion_detallada_caja_transferencia=explicacionCajaTranferencia,
            organo_direccion=organoDireccion,
            explicacion_detallada_organo_direccion=explicacionOrganoDireccion,
            rodamiento_neumaticos=rodamientoNeumaticos,
            explicacion_detallada_rodamiento_neumaticos=ExplicacionRodamientoNeumaticos,
            direccion_asistida=direccionAsistida,
            explicacion_detallada_direccion_asistida=explicacionDireccionAsistida,
            bomba_direccion_asistida=bombaDireccionAsistida,
            explicacion_detallada_bomba_direccion_asistida=explicacionbombaDireccionAsistida,
            sistema_frenado=sistemaFrenado,
            explicacion_detallada_sistema_frenado=explicacionSistemaFrenado,
            sistema_refrigeracion=sistemaRefrigeracion,
            explicacion_detallada_sistema_refrigeracion=explicacionSistemaRefrigeracion,
            sistema_calefaccion=sistemaCalefaccion,
            explicacion_detallada_sistema_calefaccion=explicacionSistemaCalefaccion,
            aire_acondicionado=aireAcondicionado,
            explicacion_detallada_aire_acondicionado=expliacionAireAcondicionado,
            abs_esp=AbsEsp,
            explicacion_detallada_abs_esp=explicacionAbsEsp,
            cuadro_instrumentos=cuadroInstrumentos,
            explicacion_detallada_cuadro_instrumentos=explicacionCuadroInstrumentos,
            limpiaparabrisas=limpiaParabrisas,
            explicacion_detallada_limpiaparabrisas=explicacionLimpiaParabrisas,
            bomba_limpiaparabrisas=bombaLimpiaparabrisas,
            explicacion_detallada_bomba_limpiaparabrisas=explicacionbombaLimpiaparabrisas,
            sistema_electrico=sistemaElectrico,
            explicacion_detallada_sistema_electrico=explicacionSistemaElectrico,
            cierre_centralizado=cierreCentralizado,
            explicacion_detallada_cierre_centralizado=expliacionCierreCentralizado,
            alumbrado_señalizacion=alumbradoSeñalizacion,
            explicacion_detallada_alumbrado_señalizacion=expliacionAlumbradoSeñalizacion,
            radio_lectorCD=radioLector,
            explicacion_detallada_radio_lectorCD=explicacionRadioLector,
            navegador=navegador,
            explicacion_detallada_navegador=explicacionNavegador,
            elevalunas_electrico=elevalunasElectrico,
            explicacion_detallada_elevalunas_electrico=explicacionElevalunasElectrico,
            airbag=airBag,
            explicacion_detallada_airbag=explicacionAirBag,
            antirrobo=antirrobo,
            explicacion_detallada_antirrobo=explicacionAntirrobo,
            techo_solar=techoSolar,
            explicacion_detallada_techo_solar=expliacionTechoSolar
        )

        datosVehiculo.save()
        suplementos.save()
        datosDelComprador.save()
        documentacion.save()
        mantenimiento.save()
        examenVisual.save()

        insercion = Insercion(
            usuario=self.request.user,
            concesionario=concesionario,
            insercion_de_Vehiculo=nombreComercial,
            duracion_del_contrato=duracionContrato
        )

        insercion.datos_del_Vehiculo = datosVehiculo
        insercion.suplementos = suplementos
        insercion.datos_del_comprador = datosDelComprador
        insercion.documentacion = documentacion
        insercion.mantenimiento = mantenimiento
        insercion.examen_visual = examenVisual

        insercion.save()
        messages.success(self.request, 'Inserción Añadida Exitosamente')
        return redirect('core:contrato')

# Vista de contrato
class FormContratoView(LoginRequiredMixin, ListView):
    model = Insercion
    template_name = 'contrato.html'
    context_object_name = 'query'
    def get_queryset(self):
        queryset = self.model.objects.filter(usuario=self.request.user).order_by('-id')
        return queryset

    def post(self, *args, **kwargs):
        insercion_pk = self.request.POST['insercion']
        contratoLocales = self.request.POST['contratoLocales']
        fecha = self.request.POST['fecha']
        firmante = self.request.POST['firmante']
        nacido = self.request.POST['nacido']
        fechaNacimiento = self.request.POST['fechaNacimiento']
        residenciaSede = self.request.POST['residenciaSede']
        telefono = self.request.POST['telefono']
        profesion = self.request.POST['profesion']
        CifNif = self.request.POST['CifNif']
        vendedor = self.request.POST['vendedor']
        marca = self.request.POST['marca']
        version = self.request.POST['version']
        modelo = self.request.POST['modelo']
        bastidor = self.request.POST['bastidor']
        estadoEncontrado = self.request.POST['estadoEncontrado']
        estadoEncontradoDescripcion = self.request.POST['estadoEncontradoDescripcion']
        marceEmpresa = self.request.POST['marceEmpresa']
        versionEmpresa = self.request.POST['versionEmpresa']
        modeloEmpresa = self.request.POST['modeloEmpresa']
        bastidorEmpresa = self.request.POST['bastidorEmpresa']
        fechaPrimeraMatriculacion = self.request.POST['fechaPrimeraMatriculacion']
        equivalenteAcordado = self.request.POST['equivalenteAcordado']
        equivalenteAcordadoMonto = self.request.POST['equivalenteAcordadoMonto']
        abonadoComprador = self.request.POST['abonadoComprador']
        abonadoCompradorMonto = self.request.POST['abonadoCompradorMonto']
        if self.request.POST['PrecioAcordado'] and int(self.request.POST['PrecioAcordado']) > 0:
            PrecioAcordado = self.request.POST['PrecioAcordado']
        else:
            PrecioAcordado = 0
        if self.request.POST['valorVehiculoRetirado'] and int(self.request.POST['valorVehiculoRetirado']) > 0:
            valorVehiculoRetirado = self.request.POST['valorVehiculoRetirado']
        else:
            valorVehiculoRetirado = 0
        if self.request.POST['depostoGarantiaPagado'] and int(self.request.POST['depostoGarantiaPagado']) > 0:
            depostoGarantiaPagado = self.request.POST['depostoGarantiaPagado']
        else:
            depostoGarantiaPagado = 0
        sociedadFinanciera = self.request.POST['sociedadFinanciera']
        nroProtocolo = self.request.POST['nroProtocolo']
        importaFinanciado = self.request.POST['importaFinanciado']
        gastosInstruccionSello = self.request.POST['gastosInstruccionSello']
        nroPlazos = self.request.POST['nroPlazos']
        importePlazos = self.request.POST['importePlazos']
        lugar = self.request.POST['lugar']
        fecha2 = self.request.POST['fecha2']

        total = int(PrecioAcordado) - (int(valorVehiculoRetirado) + int(depostoGarantiaPagado))

        contrato = Contrato(
            usuario=self.request.user,
            contratoLocales=contratoLocales,
            fecha=fecha,
            firmante=firmante,
            nacido=nacido,
            fechaNacimiento=fechaNacimiento,
            residenciaSede=residenciaSede,
            telefono=telefono,
            profesion=profesion,
            CifNif=CifNif,
            vendedor=vendedor,
            marca=marca,
            version=version,
            modelo=modelo,
            bastidor=bastidor,
            estadoEncontrado=estadoEncontrado,
            estadoEncontradoDescripcion=estadoEncontradoDescripcion,
            marceEmpresa=marceEmpresa,
            versionEmpresa=versionEmpresa,
            modeloEmpresa=modeloEmpresa,
            bastidorEmpresa=bastidorEmpresa,
            fechaPrimeraMatriculacion=fechaPrimeraMatriculacion,
            equivalenteAcordado=equivalenteAcordado,
            equivalenteAcordadoMonto=equivalenteAcordadoMonto,
            abonadoComprador=abonadoComprador,
            abonadoCompradorMonto=abonadoCompradorMonto,
            PrecioAcordado=PrecioAcordado,
            valorVehiculoRetirado=valorVehiculoRetirado,
            depostoGarantiaPagado=depostoGarantiaPagado,
            sociedadFinanciera=sociedadFinanciera,
            nroProtocolo=nroProtocolo,
            importaFinanciado=importaFinanciado,
            gastosInstruccionSello=gastosInstruccionSello,
            nroPlazos=nroPlazos,
            importePlazos=importePlazos,
            lugar=lugar,
            fecha2=fecha2,
            total=total
        )
        contrato.save()

        insercion = Insercion.objects.get(pk=insercion_pk)
        insercion.contrato = contrato
        insercion.save()

        messages.success(self.request, 'Contrato añadido exitosamente')
        return redirect('core:user')

class InsercionEditView(LoginRequiredMixin, DetailView):
    model = Insercion
    template_name = 'insercionedit.html'
    context_object_name = 'insercion'

    def post(self, *args, **kwargs):
        idPost = self.request.POST['id']

        # POLITICAS Y PRIVACIDAD:
        concesionario = self.request.POST['concesionario']

        # INSERCION DE VEHICULOS
        nombreComercial = self.request.POST['nombreComercial']

        # DATOS DEL VEHICULO
        matricula = self.request.POST['matricula']
        transmision = self.request.POST['transmision']
        marca = self.request.POST['marca']
        modelo = self.request.POST['modelo']
        alimentacion = self.request.POST['alimentacion']
        claseControl = self.request.POST['claseControl']
        primeraMatricula = self.request.POST['primeraMatricula']
        version = self.request.POST['version']
        potenciaKW = self.request.POST['potenciaKW']
        nroPropietariosPrivados = self.request.POST['nroPropietariosPrivados']
        nroPropietariosProfesionales = self.request.POST['nroPropietariosProfesionales']
        cilindrada = self.request.POST['cilindrada']
        bastidor = self.request.POST['bastidor']
        color = self.request.POST['color']
        fechaEntrega = self.request.POST['fechaEntrega']
        fechaInicio = self.request.POST['fechaInicio']
        fechaActivacion = self.request.POST['fechaActivacion']

        # suplementos
        cuatroxcuatro = self.request.POST['cuatroxcuatro']
        cambioautomatico = self.request.POST['cambioautomatico']
        vehiculoComercial = self.request.POST['vehiculoComercial']
        superCar = self.request.POST['superCar']
        suv = self.request.POST['suv']
        cobertura = self.request.POST['cobertura']

        # DATOS DEL COMPRADOR
        nombreCompleto = self.request.POST['nombreCompleto']
        direccion = self.request.POST['direccion']
        codigoPostal = self.request.POST['codigoPostal']
        numeroTelefono = self.request.POST['numeroTelefono']
        localidad = self.request.POST['localidad']
        numeroMovil = self.request.POST['numeroMovil']
        email = self.request.POST['email']
        documentoIdentidad = self.request.POST['documentoIdentidad']

        # DURACION DEL CONTRATO
        duracionContrato = self.request.POST['duracionContrato']

        # DOCUMENTACION:
        try:
            ruedaRepuesto1 = self.request.POST['ruedaRepuesto1']
        except:
            ruedaRepuesto1 = 0
        try:
            kitInflado = self.request.POST['kitInflado']
        except:
            kitInflado = 0
        try:
            trianguloEmergencia = self.request.POST['trianguloEmergencia']
        except:
            trianguloEmergencia = 0
        try:
            gato = self.request.POST['gato']
        except:
            gato = 0
        try:
            chalecoAltaVelocidad = self.request.POST['chalecoAltaVelocidad']
        except:
            chalecoAltaVelocidad = 0
        try:
            kitBombillas = self.request.POST['kitBombillas']
        except:
            kitBombillas = 0
        try:
            kitBombillasFusibles = self.request.POST['kitBombillasFusibles']
        except:
            kitBombillasFusibles = 0
        try:
            duplicadoLlaves = self.request.POST['duplicadoLlaves']
        except:
            duplicadoLlaves = 0
        try:
            codCard = self.request.POST['codCard']
        except:
            codCard = 0
        try:
            libreUsoMantenimiento = self.request.POST['libreUsoMantenimiento'] = 0
        except:
            libreUsoMantenimiento = 0
        try:
            fichaTecnica = self.request.POST['fichaTecnica']
        except:
            fichaTecnica= 0
        try:
            permisoCirculacion = self.request.POST['permisoCirculacion']
        except:
            permisoCirculacion= 0
        try:
            fechaITV = self.request.POST['fechaITV']
        except:
            fechaITV = 0

        # MANTENIMIENTO:
        estadoRevisiones = self.request.POST['estadoRevisiones']
        mantenimientoPrevioEntrega = self.request.POST['mantenimientoPrevioEntrega']
        correaServicio = self.request.POST['correaServicio']
        estadoBateria = self.request.POST['estadoBateria']
        correaDistribucion = self.request.POST['correaDistribucion']
        ultimoMantenimiento = self.request.POST['ultimoMantenimiento']
        proximoMantenimiento = self.request.POST['proximoMantenimiento']
        ultimaITV = self.request.POST['ultimaITV']
        itv = self.request.POST['itv']

        # EXAMEN VISUAL:
        carroceria = self.request.POST['carroceria']
        descripcionCarroceria = self.request.POST['descripcionCarroceria']
        habitaculoTapiceria = self.request.POST['habitaculoTapiceria']
        descripcionHabitaculoTapiceria = self.request.POST['descripcionHabitaculoTapiceria']
        habitaculoTapiceria2 = self.request.POST['habitaculoTapiceria2']
        descripcionHabitaculoTapiceria2 = self.request.POST['descripcionHabitaculoTapiceria2']
        asientoRevestimientoAsiento = self.request.POST['asientoRevestimientoAsiento']
        descripcionAsientoRevestimientoAsiento = self.request.POST['descripcionAsientoRevestimientoAsiento']
        neumaticosDelanteros = self.request.POST['neumaticosDelanteros']
        descripcionNeumaticosDelanteros = self.request.POST['descripcionNeumaticosDelanteros']
        neumaticosTraseros = self.request.POST['neumaticosTraseros']
        descripcionNeumaticosTraseros = self.request.POST['descripcionNeumaticosTraseros']
        volanteMotor = self.request.POST['volanteMotor']
        descripcionVolanteMotor = self.request.POST['descripcionVolanteMotor']
        motor = self.request.POST['motor']
        Explicacionmotor = self.request.POST['Explicacionmotor']
        sistemaEscape = self.request.POST['sistemaEscape']
        explicacionsistemaEscape = self.request.POST['explicacionsistemaEscape']
        embrague = self.request.POST['embrague']
        descripcionEmbrague = self.request.POST['descripcionEmbrague']
        alimentacionInyeccion = self.request.POST['alimentacionInyeccion']
        explicacionAlimentacionInyeccion = self.request.POST['explicacionAlimentacionInyeccion']
        cambio = self.request.POST['cambio']
        explicacionCambio = self.request.POST['explicacionCambio']
        motorArranqueAlternador = self.request.POST['motorArranqueAlternador']
        explicacionMotorArranqueAlternador = self.request.POST['explicacionMotorArranqueAlternador']
        diferencialRepartidor = self.request.POST['diferencialRepartidor']
        explicacionDiferencialRepartidor = self.request.POST['explicacionDiferencialRepartidor']
        cajaTranferencia = self.request.POST['cajaTranferencia']
        explicacionCajaTranferencia = self.request.POST['explicacionCajaTranferencia']
        organoDireccion = self.request.POST['organoDireccion']
        explicacionOrganoDireccion = self.request.POST['explicacionOrganoDireccion']
        rodamientoNeumaticos = self.request.POST['rodamientoNeumaticos']
        ExplicacionRodamientoNeumaticos = self.request.POST['ExplicacionRodamientoNeumaticos']
        direccionAsistida = self.request.POST['direccionAsistida']
        explicacionDireccionAsistida = self.request.POST['explicacionDireccionAsistida']
        bombaDireccionAsistida = self.request.POST['bombaDireccionAsistida']
        explicacionbombaDireccionAsistida = self.request.POST['explicacionbombaDireccionAsistida']
        sistemaFrenado = self.request.POST['sistemaFrenado']
        explicacionSistemaFrenado = self.request.POST['explicacionSistemaFrenado']
        sistemaRefrigeracion = self.request.POST['sistemaRefrigeracion']
        explicacionSistemaRefrigeracion = self.request.POST['explicacionSistemaRefrigeracion']
        sistemaCalefaccion = self.request.POST['sistemaCalefaccion']
        explicacionSistemaCalefaccion = self.request.POST['explicacionSistemaCalefaccion']
        aireAcondicionado = self.request.POST['aireAcondicionado']
        expliacionAireAcondicionado = self.request.POST['expliacionAireAcondicionado']
        AbsEsp = self.request.POST['AbsEsp']
        explicacionAbsEsp = self.request.POST['explicacionAbsEsp']
        cuadroInstrumentos = self.request.POST['cuadroInstrumentos']
        explicacionCuadroInstrumentos = self.request.POST['explicacionCuadroInstrumentos']
        limpiaParabrisas = self.request.POST['limpiaParabrisas']
        explicacionLimpiaParabrisas = self.request.POST['explicacionLimpiaParabrisas']
        bombaLimpiaparabrisas = self.request.POST['bombaLimpiaparabrisas']
        explicacionbombaLimpiaparabrisas = self.request.POST['explicacionbombaLimpiaparabrisas']
        sistemaElectrico = self.request.POST['sistemaElectrico']
        explicacionSistemaElectrico = self.request.POST['explicacionSistemaElectrico']
        cierreCentralizado = self.request.POST['cierreCentralizado']
        expliacionCierreCentralizado = self.request.POST['expliacionCierreCentralizado']
        alumbradoSeñalizacion = self.request.POST['alumbradoSeñalizacion']
        expliacionAlumbradoSeñalizacion = self.request.POST['expliacionAlumbradoSeñalizacion']
        radioLector = self.request.POST['radioLector']
        explicacionRadioLector = self.request.POST['explicacionRadioLector']
        navegador = self.request.POST['navegador']
        explicacionNavegador = self.request.POST['explicacionNavegador']
        elevalunasElectrico = self.request.POST['elevalunasElectrico']
        explicacionElevalunasElectrico = self.request.POST['explicacionElevalunasElectrico']
        airBag = self.request.POST['airBag']
        explicacionAirBag = self.request.POST['explicacionAirBag']
        antirrobo = self.request.POST['antirrobo']
        explicacionAntirrobo = self.request.POST['explicacionAntirrobo']
        techoSolar = self.request.POST['techoSolar']
        expliacionTechoSolar = self.request.POST['expliacionTechoSolar']

        insercion = Insercion.objects.get(pk=idPost)
        insercion.concesionario = concesionario
        insercion.insercion_de_Vehiculo = nombreComercial

        # DATOS DEL VEHICULO SAVE
        try:
            datosVehiculo = DatosVehiculo.objects.get(pk=insercion.datos_del_Vehiculo.pk)
        except AttributeError:
            datosVehiculo = DatosVehiculo.objects.create()
        datosVehiculo.matricula = matricula
        datosVehiculo.transmision = transmision
        datosVehiculo.marca = marca
        datosVehiculo.modelo = modelo
        datosVehiculo.alimentacion = alimentacion
        datosVehiculo.clase_de_cont = claseControl
        try:
            datosVehiculo.prime_matr = primeraMatricula
        except:
            pass
        datosVehiculo.version = version
        datosVehiculo.potencia_KW = potenciaKW
        datosVehiculo.nro_propietarios_Privados = nroPropietariosPrivados
        datosVehiculo.nro_propietarios_profesionales = nroPropietariosProfesionales
        datosVehiculo.cilindrada = cilindrada
        datosVehiculo.bastidor = bastidor
        datosVehiculo.color = color
        try:
            datosVehiculo.fecha_entrega = fechaEntrega
        except:
            pass

        try:
            datosVehiculo.fecha_inicio = fechaInicio
        except:
            pass
        try:
            datosVehiculo.fecha_activacion = fechaActivacion
        except:
            pass
        datosVehiculo.save()

        # SUPLEMENTOS SAVE
        try:
            suplementos = Suplemento.objects.get(pk=insercion.suplementos.pk)
        except AttributeError:
            suplementos = Suplemento.objects.create()
        suplementos.cuatro_por_cuatro = cuatroxcuatro
        suplementos.super_Car = superCar
        suplementos.cambio_autom = cambioautomatico
        suplementos.suv = suv
        suplementos.vehiculo_comercial = vehiculoComercial
        suplementos.cobertura = cobertura
        suplementos.save()

        # DATOS DEL COMPRADOR SAVE
        try:
            datos_comprador = DatosComprador.objects.get(pk=insercion.datos_del_comprador.pk)
        except AttributeError:
            datos_comprador = DatosComprador.objects.create()
        datos_comprador.nombre_Completo = nombreCompleto
        datos_comprador.codigo_postal = codigoPostal
        datos_comprador.localidad_Provincia_Pais = localidad
        datos_comprador.email = email
        datos_comprador.direccion = direccion
        datos_comprador.numero_de_telefono = numeroTelefono
        datos_comprador.numero_de_movil = numeroMovil
        datos_comprador.documento_identidad = documentoIdentidad
        datos_comprador.save()

        # DOCUMENTACION SAVE
        try:
            documentacion = Documentacion.objects.get(pk=insercion.documentacion.pk)
        except AttributeError:
            documentacion = Documentacion.objects.create()
        documentacion.rueda_repuesto1 = ruedaRepuesto1
        documentacion.duplicado_llaves = duplicadoLlaves
        documentacion.kit_inflado = kitInflado
        documentacion.triangulo_emergencia = trianguloEmergencia
        documentacion.gato = gato
        documentacion.chaleco_alta_visibilidad = chalecoAltaVelocidad
        documentacion.kit_bombillas = kitBombillas
        documentacion.kit_bombillas_fusibles = kitBombillasFusibles
        documentacion.cod_card = codCard
        documentacion.libre_uso_mantenimiento = libreUsoMantenimiento
        documentacion.ficha_tecnica = fichaTecnica
        documentacion.permiso_circulacion = permisoCirculacion
        try:
            documentacion.fecha = fechaITV
        except:
            pass
        documentacion.itv = itv
        documentacion.save()

        # MANTENIMIENTO SAVE
        try:
            mantenimiento = Mantenimiento.objects.get(pk=insercion.mantenimiento.pk)
        except AttributeError:
            mantenimiento = Mantenimiento.objects.create()
        mantenimiento.estado_revisiones = estadoRevisiones
        mantenimiento.mantenimiento_previo_entrega = mantenimientoPrevioEntrega
        mantenimiento.correa_servicio = correaServicio
        mantenimiento.estado_bateria = estadoBateria
        mantenimiento.correa_distribucion = correaDistribucion
        try:
            mantenimiento.ultimo_mantenimiento = ultimoMantenimiento
        except:
            pass
        try:
            mantenimiento.proximo_mantenimiento = proximoMantenimiento
        except:
            pass
        try:
            mantenimiento.ultima_ITV = ultimaITV
        except:
            pass
        mantenimiento.save()

        # EXAMEN VISUAL
        try:
            examenVisual = ExamenVisual.objects.get(pk=insercion.examen_visual.pk)
        except:
            examenVisual = ExamenVisual.objects.create()
        examenVisual.carroceria = carroceria
        examenVisual.descripcion_carroceria = descripcionCarroceria
        examenVisual.habitaculo_tapiceria_1 = habitaculoTapiceria
        examenVisual.descripcion_habitaculo_tapiceria_1 = descripcionHabitaculoTapiceria
        examenVisual.habitaculo_tapiceria_2 = habitaculoTapiceria2
        examenVisual.descripcion_habitaculo_tapiceria_2 = descripcionHabitaculoTapiceria2
        examenVisual.asiento_revestimiento_asiento = asientoRevestimientoAsiento
        examenVisual.descripcion_asiento_revestimiento_asiento = descripcionAsientoRevestimientoAsiento
        examenVisual.neumaticos_delanteros = neumaticosDelanteros
        examenVisual.descripcion_neumaticos_delanteros = descripcionNeumaticosDelanteros
        examenVisual.neumaticos_traseros = neumaticosTraseros
        examenVisual.descripcion_neumaticos_traseros = descripcionNeumaticosTraseros
        examenVisual.volante_motor = volanteMotor
        examenVisual.explicacion_detallada_volante_motor = descripcionVolanteMotor
        examenVisual.motor = motor
        examenVisual.explicacion_detallada_motor = Explicacionmotor
        examenVisual.sistema_escape = sistemaEscape
        examenVisual.explicacion_detallada_sistema_escape = explicacionsistemaEscape
        examenVisual.embrague = embrague
        examenVisual.explicacion_detallada_embrague = descripcionEmbrague
        examenVisual.alimentacion_inyeccion = alimentacionInyeccion
        examenVisual.explicacion_detallada_alimentacion_inyeccion = explicacionAlimentacionInyeccion
        examenVisual.cambio = cambio
        examenVisual.explicacion_detallada_cambio = explicacionCambio
        examenVisual.moto_arranque_alternador = motorArranqueAlternador
        examenVisual.explicacion_detallada_moto_arranque_alternador = explicacionMotorArranqueAlternador
        examenVisual.diferencial_repartidor = diferencialRepartidor
        examenVisual.explicacion_detallada_diferencial_repartidor = explicacionDiferencialRepartidor
        examenVisual.caja_transferencia = cajaTranferencia
        examenVisual.explicacion_detallada_caja_transferencia = explicacionCajaTranferencia
        examenVisual.organo_direccion = organoDireccion
        examenVisual.explicacion_detallada_organo_direccion = explicacionOrganoDireccion
        examenVisual.rodamiento_neumaticos = rodamientoNeumaticos
        examenVisual.explicacion_detallada_rodamiento_neumaticos = ExplicacionRodamientoNeumaticos
        examenVisual.direccion_asistida = direccionAsistida
        examenVisual.explicacion_detallada_direccion_asistida = explicacionDireccionAsistida
        examenVisual.bomba_direccion_asistida = bombaDireccionAsistida
        examenVisual.explicacion_detallada_bomba_direccion_asistida = explicacionbombaDireccionAsistida
        examenVisual.sistema_frenado = sistemaFrenado
        examenVisual.explicacion_detallada_sistema_frenado = explicacionSistemaFrenado
        examenVisual.sistema_refrigeracion = sistemaRefrigeracion
        examenVisual.explicacion_detallada_sistema_refrigeracion = explicacionSistemaRefrigeracion
        examenVisual.sistema_calefaccion = sistemaCalefaccion
        examenVisual.explicacion_detallada_sistema_calefaccion = explicacionSistemaCalefaccion
        examenVisual.aire_acondicionado = aireAcondicionado
        examenVisual.explicacion_detallada_aire_acondicionado = expliacionAireAcondicionado
        examenVisual.abs_esp = AbsEsp
        examenVisual.explicacion_detallada_abs_esp = explicacionAbsEsp
        examenVisual.cuadro_instrumentos = cuadroInstrumentos
        examenVisual.explicacion_detallada_cuadro_instrumentos = explicacionCuadroInstrumentos
        examenVisual.limpiaparabrisas = limpiaParabrisas
        examenVisual.explicacion_detallada_limpiaparabrisas = explicacionLimpiaParabrisas
        examenVisual.bomba_limpiaparabrisas = bombaLimpiaparabrisas
        examenVisual.explicacion_detallada_bomba_limpiaparabrisas = explicacionbombaLimpiaparabrisas
        examenVisual.sistema_electrico = sistemaElectrico
        examenVisual.explicacion_detallada_sistema_electrico = explicacionSistemaElectrico
        examenVisual.cierre_centralizado = cierreCentralizado
        examenVisual.explicacion_detallada_cierre_centralizado = expliacionCierreCentralizado
        examenVisual.alumbrado_señalizacion = alumbradoSeñalizacion
        examenVisual.explicacion_detallada_alumbrado_señalizacion = expliacionAlumbradoSeñalizacion
        examenVisual.radio_lectorCD = radioLector
        examenVisual.explicacion_detallada_radio_lectorCD = explicacionRadioLector
        examenVisual.navegador = navegador
        examenVisual.explicacion_detallada_navegador = explicacionNavegador
        examenVisual.elevalunas_electrico = elevalunasElectrico
        examenVisual.explicacion_detallada_elevalunas_electrico = explicacionElevalunasElectrico
        examenVisual.airbag = airBag
        examenVisual.explicacion_detallada_airbag = explicacionAirBag
        examenVisual.antirrobo = antirrobo
        examenVisual.explicacion_detallada_antirrobo = explicacionAntirrobo
        examenVisual.techo_solar = techoSolar
        examenVisual.explicacion_detallada_techo_solar = expliacionTechoSolar
        examenVisual.save()

        insercion.datos_del_Vehiculo = datosVehiculo
        insercion.suplementos = suplementos
        insercion.datos_del_comprador = datos_comprador
        insercion.documentacion = documentacion
        insercion.mantenimiento = mantenimiento
        insercion.examen_visual = examenVisual
        insercion.save()
        messages.success(self.request, 'Inserción Editada Exitosamente')
        return redirect('core:editar-insercion', pk=idPost)

class ContratoEditView(LoginRequiredMixin, DetailView):
    model = Insercion
    template_name = 'contratoEdit.html'
    context_object_name = 'contrato'

    def post(self, *args, **kwargs):
        insercion_pk = self.request.POST['insercion']
        contrato_pk =self.request.POST['contrato']
        contratoLocales = self.request.POST['contratoLocales']
        fecha = self.request.POST['fecha']
        firmante = self.request.POST['firmante']
        nacido = self.request.POST['nacido']
        fechaNacimiento = self.request.POST['fechaNacimiento']
        residenciaSede = self.request.POST['residenciaSede']
        telefono = self.request.POST['telefono']
        profesion = self.request.POST['profesion']
        CifNif = self.request.POST['CifNif']
        vendedor = self.request.POST['vendedor']
        marca = self.request.POST['marca']
        version = self.request.POST['version']
        modelo = self.request.POST['modelo']
        bastidor = self.request.POST['bastidor']
        estadoEncontrado = self.request.POST['estadoEncontrado']
        estadoEncontradoDescripcion = self.request.POST['estadoEncontradoDescripcion']
        marceEmpresa = self.request.POST['marceEmpresa']
        versionEmpresa = self.request.POST['versionEmpresa']
        modeloEmpresa = self.request.POST['modeloEmpresa']
        bastidorEmpresa = self.request.POST['bastidorEmpresa']
        fechaPrimeraMatriculacion = self.request.POST['fechaPrimeraMatriculacion']
        equivalenteAcordado = self.request.POST['equivalenteAcordado']
        equivalenteAcordadoMonto = self.request.POST['equivalenteAcordadoMonto']
        abonadoComprador = self.request.POST['abonadoComprador']
        abonadoCompradorMonto = self.request.POST['abonadoCompradorMonto']
        if self.request.POST['PrecioAcordado'] and int(self.request.POST['PrecioAcordado']) > 0:
            PrecioAcordado = self.request.POST['PrecioAcordado']
        else:
            PrecioAcordado = 0
        if self.request.POST['valorVehiculoRetirado'] and int(self.request.POST['valorVehiculoRetirado']) > 0:
            valorVehiculoRetirado = self.request.POST['valorVehiculoRetirado']
        else:
            valorVehiculoRetirado = 0
        if self.request.POST['depostoGarantiaPagado'] and int(self.request.POST['depostoGarantiaPagado']) > 0:
            depostoGarantiaPagado = self.request.POST['depostoGarantiaPagado']
        else:
            depostoGarantiaPagado = 0
        sociedadFinanciera = self.request.POST['sociedadFinanciera']
        nroProtocolo = self.request.POST['nroProtocolo']
        importaFinanciado = self.request.POST['importaFinanciado']
        gastosInstruccionSello = self.request.POST['gastosInstruccionSello']
        nroPlazos = self.request.POST['nroPlazos']
        importePlazos = self.request.POST['importePlazos']
        lugar = self.request.POST['lugar']
        fecha2 = self.request.POST['fecha2']

        total = int(PrecioAcordado) - (int(valorVehiculoRetirado) + int(depostoGarantiaPagado))

        contrato = Contrato.objects.get(pk=contrato_pk)
        contrato.usuario = self.request.user
        contrato.contratoLocales = contratoLocales
        contrato.fecha = fecha
        contrato.firmante = firmante
        contrato.nacido = nacido
        contrato.fechaNacimiento = fechaNacimiento
        contrato.residenciaSede = residenciaSede
        contrato.telefono = telefono
        contrato.profesion = profesion
        contrato.CifNif = CifNif
        contrato.vendedor = vendedor
        contrato.marca = marca
        contrato.version = version
        contrato.modelo = modelo
        contrato.bastidor = bastidor
        contrato.estadoEncontrado = estadoEncontrado
        contrato.estadoEncontradoDescripcion = estadoEncontradoDescripcion
        contrato.marceEmpresa = marceEmpresa
        contrato.versionEmpresa = versionEmpresa
        contrato.modeloEmpresa = modeloEmpresa
        contrato.bastidorEmpresa = bastidorEmpresa
        contrato.fechaPrimeraMatriculacion = fechaPrimeraMatriculacion
        contrato.equivalenteAcordado = equivalenteAcordado
        contrato.equivalenteAcordadoMonto = equivalenteAcordadoMonto
        contrato.abonadoComprador = abonadoComprador
        contrato.abonadoCompradorMonto = abonadoCompradorMonto
        contrato.PrecioAcordado = PrecioAcordado
        contrato.valorVehiculoRetirado = valorVehiculoRetirado
        contrato.depostoGarantiaPagado = depostoGarantiaPagado
        contrato.sociedadFinanciera = sociedadFinanciera
        contrato.nroProtocolo = nroProtocolo
        contrato.importaFinanciado = importaFinanciado
        contrato.gastosInstruccionSello = gastosInstruccionSello
        contrato.nroPlazos = nroPlazos
        contrato.importePlazos = importePlazos
        contrato.lugar = lugar
        contrato.fecha2 = fecha2
        contrato.total = total
        contrato.save()

        insercion = Insercion.objects.get(pk=insercion_pk)
        insercion.contrato = contrato
        insercion.save()

        messages.success(self.request, 'Contrato Editado Exitosamente')
        return redirect('core:editar-contrato', pk=insercion_pk)

class UserView(LoginRequiredMixin, ListView):
    model = Insercion
    template_name = 'usuario.html'
    context_object_name = 'query'

    def get_queryset(self):
        queryset = {'insercion': Insercion.objects.filter(usuario=self.request.user).order_by('-id'), 
                    'contrato': Contrato.objects.filter(usuario=self.request.user).order_by('-id'),
                    }
        return queryset

class UserProfile(LoginRequiredMixin, View):
    model = User
    def get(self, request, *args, **kwargs):
        user = self.model.objects.get(pk=self.request.user.pk)
        context = { 'user': user }
        return render(self.request, 'perfilUsuario.html', context)

    def post(self, request, *args, **kwargs):
        archivo = self.request.FILES.get('image')
        user = User.objects.get(pk=self.request.user.pk)
        if user.imagen != archivo:
            user.imagen.delete(save=False)
        user.imagen = archivo
        user.save()
        context = { 'user': user }
        return redirect('core:user-profile')

def pdfInsercion(request, pk):

    def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
            # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    try:
        template = get_template('pdf.html')
        insercion = Insercion.objects.filter(pk=pk)
        if insercion.exists():
            context = {
                'insercion': insercion,
                'icon': '{}{}'.format(settings.STATIC_URL, 'img/autos.png'),
                'icon1': '{}{}'.format(settings.STATIC_URL, 'img/uncheck.png'),
                'icon2': '{}{}'.format(settings.STATIC_URL, 'img/logo-hosho.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=link_callback)
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        else:
            return HttpResponse('Consulta invalida')
    except:
        pass
    HttpResponseRedirect(reverse_lazy('core:inicio'))

def pdfContrato(request, pk):

    def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
            # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    try:
        template = get_template('pdfContrato.html')
        contrato = Insercion.objects.filter(pk=pk)
        if contrato.exists():
            context = {
                'contrato': contrato,
                'icon': '{}{}'.format(settings.STATIC_URL, 'img/uncheck.png'),
                'icon2': '{}{}'.format(settings.STATIC_URL, 'img/logo-hosho.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response, link_callback=link_callback)
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        else:
            return HttpResponse('Consulta invalida')
    except:
        pass
    HttpResponseRedirect(reverse_lazy('core:inicio'))

def inicio(request):
    if request.user.is_authenticated:
        return redirect('core:user')
    else:
        return redirect('accounts/login')

def search(request):
    if request.method=='POST':
        matricula = request.POST['matricula']
        insercion = Insercion.objects.filter(datos_del_Vehiculo__matricula__icontains=matricula)
        query = {
            'insercion': insercion
        }
        return render(request, 'usuario.html', query)
    else:
        return redirect('core:user')