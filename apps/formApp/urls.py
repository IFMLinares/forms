from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    FormInsercion,
    FormContrato,
    inicio
)

app_name = 'core'

urlpatterns = [
    path('insercion/', FormInsercion.as_view(), name='insercion'),
    path('contrato/', FormContrato.as_view(), name='contrato'),
    path('', inicio, name='inicio'),
]

