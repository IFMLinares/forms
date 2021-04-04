from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    FormInsercionView,
    FormContratoView,
    PdfView,
    inicio
)

app_name = 'core'

urlpatterns = [
    path('insercion/', FormInsercionView.as_view(), name='insercion'),
    path('contrato/', FormContratoView.as_view(), name='contrato'),
    path('pdf/<int:pk>/', PdfView.as_view(), name='pdf'),
    path('', inicio, name='inicio'),
]

