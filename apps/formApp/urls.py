from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    Index,
    Proteccion,
    Insercion,
    Examen,
    Documentacion,
    Condiciones
)

app_name = 'core'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('proteccion/', Proteccion.as_view(), name='proteccion'),
    path('insercion/', Insercion.as_view(), name='insercion'),
    path('examen/', Examen.as_view(), name='examen'),
    path('documentacion/', Documentacion.as_view(), name='documentacion'),
    path('condiciones/', Condiciones.as_view(), name='condiciones'),
]

