import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
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
    Contrato
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
        queryset = self.model.objects.filter(contrato='')
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
        PrecioAcordado = self.request.POST['PrecioAcordado']
        valorVehiculoRetirado = self.request.POST['valorVehiculoRetirado']
        depostoGarantiaPagado = self.request.POST['depostoGarantiaPagado']
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
        insercion.datos_del_Vehiculo.matricula = matricula
        insercion.datos_del_Vehiculo.transmision = transmision
        insercion.datos_del_Vehiculo.marca = marca
        insercion.datos_del_Vehiculo.modelo = modelo
        insercion.datos_del_Vehiculo.alimentacion = alimentacion
        insercion.datos_del_Vehiculo.clase_de_cont = claseControl
        insercion.datos_del_Vehiculo.prime_matr = primeraMatricula
        insercion.datos_del_Vehiculo.version = version
        insercion.datos_del_Vehiculo.potencia_KW = potenciaKW
        insercion.datos_del_Vehiculo.nro_propietarios_Privados = nroPropietariosPrivados
        insercion.datos_del_Vehiculo.nro_propietarios_profesionales = nroPropietariosProfesionales
        insercion.datos_del_Vehiculo.cilindrada = cilindrada
        insercion.datos_del_Vehiculo.bastidor = bastidor
        insercion.datos_del_Vehiculo.color = color
        insercion.datos_del_Vehiculo.fecha_entrega = fechaEntrega
        insercion.datos_del_Vehiculo.fecha_inicio = fechaInicio
        insercion.datos_del_Vehiculo.fecha_activacion = fechaActivacion

        # SUPLEMENTOS SAVE
        insercion.suplementos.cuatro_por_cuatro = cuatroxcuatro
        insercion.suplementos.super_Car = cambioautomatico
        insercion.suplementos.cambio_autom = vehiculoComercial
        insercion.suplementos.suv = superCar
        insercion.suplementos.vehiculo_comercial = suv
        insercion.suplementos.cobertura = cobertura

        # DATOS DEL COMPRADOR SAVE
        insercion.datos_del_comprador.nombre_Completo = nombreCompleto
        insercion.datos_del_comprador.codigo_postal = codigoPostal
        insercion.datos_del_comprador.localidad_Provincia_Pais = localidad
        insercion.datos_del_comprador.email = email
        insercion.datos_del_comprador.direccion = direccion
        insercion.datos_del_comprador.numero_de_telefono = numeroTelefono
        insercion.datos_del_comprador.numero_de_movil = numeroMovil
        insercion.datos_del_comprador.documento_identidad = documentoIdentidad

        # DOCUMENTACION SAVE
        insercion.documentacion.rueda_repuesto1 = ruedaRepuesto1
        insercion.documentacion.duplicado_llaves = duplicadoLlaves
        insercion.documentacion.kit_inflado = kitInflado
        insercion.documentacion.triangulo_emergencia = trianguloEmergencia
        insercion.documentacion.gato = gato
        insercion.documentacion.chaleco_alta_visibilidad = chalecoAltaVelocidad
        insercion.documentacion.kit_bombillas = kitBombillas
        insercion.documentacion.kit_bombillas_fusibles = kitBombillasFusibles
        insercion.documentacion.cod_card = codCard
        insercion.documentacion.libre_uso_mantenimiento = libreUsoMantenimiento
        insercion.documentacion.ficha_tecnica = fichaTecnica
        insercion.documentacion.permiso_circulacion = permisoCirculacion
        insercion.documentacion.fecha = fechaITV
        insercion.documentacion.itv = itv

        # MANTENIMIENTO SAVE
        insercion.mantenimiento.estado_revisiones = estadoRevisiones
        insercion.mantenimiento.mantenimiento_previo_entrega = mantenimientoPrevioEntrega
        insercion.mantenimiento.correa_servicio = correaServicio
        insercion.mantenimiento.estado_bateria = estadoBateria
        insercion.mantenimiento.correa_distribucion = correaDistribucion
        insercion.mantenimiento.ultimo_mantenimiento = ultimoMantenimiento
        insercion.mantenimiento.proximo_mantenimiento = proximoMantenimiento
        insercion.mantenimiento.ultima_ITV = ultimaITV

        # EXAMEN VISUAL
        insercion.examen_visual.carroceria = carroceria
        insercion.examen_visual.descripcion_carroceria = descripcionCarroceria
        insercion.examen_visual.habitaculo_tapiceria_1 = habitaculoTapiceria
        insercion.examen_visual.descripcion_habitaculo_tapiceria_1 = descripcionHabitaculoTapiceria
        insercion.examen_visual.habitaculo_tapiceria_2 = habitaculoTapiceria2
        insercion.examen_visual.descripcion_habitaculo_tapiceria_2 = descripcionHabitaculoTapiceria2
        insercion.examen_visual.asiento_revestimiento_asiento = asientoRevestimientoAsiento
        insercion.examen_visual.descripcion_asiento_revestimiento_asiento = descripcionAsientoRevestimientoAsiento
        insercion.examen_visual.neumaticos_delanteros = neumaticosDelanteros
        insercion.examen_visual.descripcion_neumaticos_delanteros = descripcionNeumaticosDelanteros
        insercion.examen_visual.neumaticos_traseros = neumaticosTraseros
        insercion.examen_visual.descripcion_neumaticos_traseros = descripcionNeumaticosTraseros
        insercion.examen_visual.volante_motor = volanteMotor
        insercion.examen_visual.explicacion_detallada_volante_motor = descripcionVolanteMotor
        insercion.examen_visual.motor = motor
        insercion.examen_visual.explicacion_detallada_motor = Explicacionmotor
        insercion.examen_visual.sistema_escape = sistemaEscape
        insercion.examen_visual.explicacion_detallada_sistema_escape = explicacionsistemaEscape
        insercion.examen_visual.embrague = embrague
        insercion.examen_visual.explicacion_detallada_embrague = descripcionEmbrague
        insercion.examen_visual.alimentacion_inyeccion = alimentacionInyeccion
        insercion.examen_visual.explicacion_detallada_alimentacion_inyeccion = explicacionAlimentacionInyeccion
        insercion.examen_visual.cambio = cambio
        insercion.examen_visual.explicacion_detallada_cambio = explicacionCambio
        insercion.examen_visual.moto_arranque_alternador = motorArranqueAlternador
        insercion.examen_visual.explicacion_detallada_moto_arranque_alternador = explicacionMotorArranqueAlternador
        insercion.examen_visual.diferencial_repartidor = diferencialRepartidor
        insercion.examen_visual.explicacion_detallada_diferencial_repartidor = explicacionDiferencialRepartidor
        insercion.examen_visual.caja_transferencia = cajaTranferencia
        insercion.examen_visual.explicacion_detallada_caja_transferencia = explicacionCajaTranferencia
        insercion.examen_visual.organo_direccion = organoDireccion
        insercion.examen_visual.explicacion_detallada_organo_direccion = explicacionOrganoDireccion
        insercion.examen_visual.rodamiento_neumaticos = rodamientoNeumaticos
        insercion.examen_visual.explicacion_detallada_rodamiento_neumaticos = ExplicacionRodamientoNeumaticos
        insercion.examen_visual.direccion_asistida = direccionAsistida
        insercion.examen_visual.explicacion_detallada_direccion_asistida = explicacionDireccionAsistida
        insercion.examen_visual.bomba_direccion_asistida = bombaDireccionAsistida
        insercion.examen_visual.explicacion_detallada_bomba_direccion_asistida = explicacionbombaDireccionAsistida
        insercion.examen_visual.sistema_frenado = sistemaFrenado
        insercion.examen_visual.explicacion_detallada_sistema_frenado = explicacionSistemaFrenado
        insercion.examen_visual.sistema_refrigeracion = sistemaRefrigeracion
        insercion.examen_visual.explicacion_detallada_sistema_refrigeracion = explicacionSistemaRefrigeracion
        insercion.examen_visual.sistema_calefaccion = sistemaCalefaccion
        insercion.examen_visual.explicacion_detallada_sistema_calefaccion = explicacionSistemaCalefaccion
        insercion.examen_visual.aire_acondicionado = aireAcondicionado
        insercion.examen_visual.explicacion_detallada_aire_acondicionado = expliacionAireAcondicionado
        insercion.examen_visual.abs_esp = AbsEsp
        insercion.examen_visual.explicacion_detallada_abs_esp = explicacionAbsEsp
        insercion.examen_visual.cuadro_instrumentos = cuadroInstrumentos
        insercion.examen_visual.explicacion_detallada_cuadro_instrumentos = explicacionCuadroInstrumentos
        insercion.examen_visual.limpiaparabrisas = limpiaParabrisas
        insercion.examen_visual.explicacion_detallada_limpiaparabrisas = explicacionLimpiaParabrisas
        insercion.examen_visual.bomba_limpiaparabrisas = bombaLimpiaparabrisas
        insercion.examen_visual.explicacion_detallada_bomba_limpiaparabrisas = explicacionbombaLimpiaparabrisas
        insercion.examen_visual.sistema_electrico = sistemaElectrico
        insercion.examen_visual.explicacion_detallada_sistema_electrico = explicacionSistemaElectrico
        insercion.examen_visual.cierre_centralizado = cierreCentralizado
        insercion.examen_visual.explicacion_detallada_cierre_centralizado = expliacionCierreCentralizado
        insercion.examen_visual.alumbrado_señalizacion = alumbradoSeñalizacion
        insercion.examen_visual.explicacion_detallada_alumbrado_señalizacion = expliacionAlumbradoSeñalizacion
        insercion.examen_visual.radio_lectorCD = radioLector
        insercion.examen_visual.explicacion_detallada_radio_lectorCD = explicacionRadioLector
        insercion.examen_visual.navegador = navegador
        insercion.examen_visual.explicacion_detallada_navegador = explicacionNavegador
        insercion.examen_visual.elevalunas_electrico = elevalunasElectrico
        insercion.examen_visual.explicacion_detallada_elevalunas_electrico = explicacionElevalunasElectrico
        insercion.examen_visual.airbag = airBag
        insercion.examen_visual.explicacion_detallada_airbag = explicacionAirBag
        insercion.examen_visual.antirrobo = antirrobo
        insercion.examen_visual.explicacion_detallada_antirrobo = explicacionAntirrobo
        insercion.examen_visual.techo_solar = techoSolar
        insercion.examen_visual.explicacion_detallada_techo_solar = expliacionTechoSolar

        insercion.save()
        messages.success(self.request, 'Inserción Añadida Exitosamente')
        return redirect('core:contrato')

class ContratoEditView(LoginRequiredMixin, DetailView):
    model = Insercion
    template_name = 'contratoEdit.html'
    context_object_name = 'contrato'

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
        PrecioAcordado = self.request.POST['PrecioAcordado']
        valorVehiculoRetirado = self.request.POST['valorVehiculoRetirado']
        depostoGarantiaPagado = self.request.POST['depostoGarantiaPagado']
        sociedadFinanciera = self.request.POST['sociedadFinanciera']
        nroProtocolo = self.request.POST['nroProtocolo']
        importaFinanciado = self.request.POST['importaFinanciado']
        gastosInstruccionSello = self.request.POST['gastosInstruccionSello']
        nroPlazos = self.request.POST['nroPlazos']
        importePlazos = self.request.POST['importePlazos']
        lugar = self.request.POST['lugar']
        fecha2 = self.request.POST['fecha2']

        total = int(PrecioAcordado) - (int(valorVehiculoRetirado) + int(depostoGarantiaPagado))

class UserView(LoginRequiredMixin, ListView):
    model = Insercion
    template_name = 'usuario.html'
    context_object_name = 'query'

    def get_queryset(self):
        queryset = {'insercion': Insercion.objects.filter(usuario=self.request.user).order_by('-id'), 
                    'contrato': Contrato.objects.filter(usuario=self.request.user).order_by('-id'),
                    }
        return queryset


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
                'icon': '{}{}'.format(settings.STATIC_URL, 'img/autos.png')
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
                'icon': '{}{}'.format(settings.STATIC_URL, 'img/uncheck.png')
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

# def add_user_logout_view(request):
    # logout(request)
    # return redirect('account_signup')

def search(request):
    if request.method=='POST':
        matricula = request.POST['matricula']
        insercion = Insercion.objects.filter(datos_del_Vehiculo__matricula=matricula)
        query = {
            'insercion': insercion
        }
        return render(request, 'usuario.html', query)
    else:
        return redirect('core:user')