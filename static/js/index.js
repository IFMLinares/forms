var politica_privacidad = document.getElementById('politica-privacidad');
var insercion_vehiculo = document.getElementById('insercion-vehiculo');
var documentos_mantenimiento = document.getElementById('documentos-mantenimiento');
var examen = document.getElementById('examen');
var condiciones_servicio = document.getElementById('condiciones-servicio');
var proteccion_datos = document.getElementById('proteccion-datos');
var anterior = document.getElementById('anterior');
var siguiente = document.getElementById('siguiente');
var form = document.getElementById('form');

$(document).ready(function () {
	$('#click1').click(function () {
		if ($('#hidden1').is(':hidden')) {
			$('#hidden1').show(500);
		} else {
			$('#hidden1').hide(500);
		}
	});
});

$(".submenu").click(function () {
	$(this).children("ul").slideToggle();
})

$("ul").click(function (ev) {
	ev.stopPropagation();
})

var count = 1
$('#siguiente').click(function (ev) {
	ev.preventDefault;
	count = count + 1;
	console.log(count);
	adelante(count);
	arriba();
	console.log(count);
})

$('#anterior').click(function (ev) {
	ev.preventDefault;
	if (count == 1) {
		count = 1
		politica_privacidad.style.display = "block";
		insercion_vehiculo.style.display = "none";
	} else {
		count = count - 1;
		atras(count);
		arriba();
		console.log(count);
	}

})


function arriba() {
	$("html, body").animate({ scrollTop: 0 }, 600);
	return false;
}

function adelante(count) {
	if (count == 2) {
		politica_privacidad.style.display = "none";
		insercion_vehiculo.style.display = "block";
		anterior.removeAttribute("disabled", "");
	} else if (count == 3) {
		insercion_vehiculo.style.display = "none";
		documentos_mantenimiento.style.display = "block";
	} else if (count == 4) {
		documentos_mantenimiento.style.display = "none";
		examen.style.display = "block";
	} else if (count == 5) {
		examen.style.display = "none";
		condiciones_servicio.style.display = "block";
	} else if (count == 6) {
		condiciones_servicio.style.display = "none";
		proteccion_datos.style.display = "block";
		siguiente.setAttribute("disabled", "");
	} else {
		proteccion_datos.style.display = "none";
		politica_privacidad.style.display = "block";
		siguiente.removeAttribute("disabled", "");
	}
}

function atras(count) {
	if (count == 1) {
		politica_privacidad.style.display = "block";
		insercion_vehiculo.style.display = "none";
		siguiente.removeAttribute("disabled", "");
		anterior.setAttribute("disabled", "");
	} else if (count == 2) {
		insercion_vehiculo.style.display = "block";
		documentos_mantenimiento.style.display = "none";
	} else if (count == 3) {
		documentos_mantenimiento.style.display = "block";
		examen.style.display = "none";
	} else if (count == 4) {
		examen.style.display = "block";
		condiciones_servicio.style.display = "none";
	} else if (count == 5) {
		condiciones_servicio.style.display = "block";
		proteccion_datos.style.display = "none";
		siguiente.removeAttribute("disabled", "");
	} else {
		proteccion_datos.style.display = "block";
		politica_privacidad.style.display = "none";
	}
}

function mostrar(pagina) {
	if (pagina == 1) {
		politica_privacidad.style.display = "block";
		insercion_vehiculo.style.display = "none";
		documentos_mantenimiento.style.display = "none";
		examen.style.display = "none";
		condiciones_servicio.style.display = "none";
		proteccion_datos.style.display = "none";
		count = 1;
		siguiente.removeAttribute("disabled", "");
		anterior.setAttribute("disabled", "");
	} else if (pagina == 2) {
		politica_privacidad.style.display = "none";
		insercion_vehiculo.style.display = "block";
		documentos_mantenimiento.style.display = "none";
		examen.style.display = "none";
		condiciones_servicio.style.display = "none";
		proteccion_datos.style.display = "none";
		count = 2;
		anterior.removeAttribute("disabled", "");
		siguiente.removeAttribute("disabled", "");
	} else if (pagina == 3) {
		politica_privacidad.style.display = "none";
		insercion_vehiculo.style.display = "none";
		documentos_mantenimiento.style.display = "block";
		examen.style.display = "none";
		condiciones_servicio.style.display = "none";
		proteccion_datos.style.display = "none";
		count = 3;
		anterior.removeAttribute("disabled", "");
		siguiente.removeAttribute("disabled", "");
	} else if (pagina == 4) {
		politica_privacidad.style.display = "none";
		insercion_vehiculo.style.display = "none";
		documentos_mantenimiento.style.display = "none";
		examen.style.display = "block";
		condiciones_servicio.style.display = "none";
		proteccion_datos.style.display = "none";
		count = 4;
		anterior.removeAttribute("disabled", "");
		siguiente.removeAttribute("disabled", "");
	} else if (pagina == 5) {
		politica_privacidad.style.display = "none";
		insercion_vehiculo.style.display = "none";
		documentos_mantenimiento.style.display = "none";
		examen.style.display = "none";
		condiciones_servicio.style.display = "block";
		proteccion_datos.style.display = "none";
		count = 5;
		anterior.removeAttribute("disabled", "");
		siguiente.removeAttribute("disabled", "");
	} else {
		politica_privacidad.style.display = "none";
		insercion_vehiculo.style.display = "none";
		documentos_mantenimiento.style.display = "none";
		examen.style.display = "none";
		condiciones_servicio.style.display = "none";
		proteccion_datos.style.display = "block";
		count = 6;
		siguiente.setAttribute("disabled", "");
		anterior.removeAttribute("disabled", "");
	}
}