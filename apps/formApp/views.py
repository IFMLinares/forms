from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'