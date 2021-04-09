from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    FormInsercionView,
    FormContratoView,
    # PdfView,
    inicio,
    pdfInsercion,
    pdfContrato,
    UserView
)

app_name = 'core'

urlpatterns = [
    path('insercion/', FormInsercionView.as_view(), name='insercion'),
    path('contrato/<pk>/', FormContratoView.as_view(), name='contrato'),
    path('usuario/', UserView.as_view(), name='user'),
    path('pdfInsercion/<pk>/', pdfInsercion, name='pdf-incersion'),
    path('pdfContrato/<pk>/', pdfContrato, name='pdf-contrato'),
    path('', inicio, name='inicio'),
]

