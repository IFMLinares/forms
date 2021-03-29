from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

class Proteccion(TemplateView):
    template_name = 'proteccion.html'

class Insercion(TemplateView):
    template_name = 'insercion.html'

class Examen(TemplateView):
    template_name = 'examen.html'

class Documentacion(TemplateView):
    template_name = 'documentacion.html'