from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    FormInsercionView,
    FormContratoView,
    # PdfView,
    inicio,
    pdfInsercion,
    pdfContrato,
    UserView,
    # add_user_logout_view,
    search,
    InsercionEditView,
    ContratoEditView
)

app_name = 'core'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('insercion/', FormInsercionView.as_view(), name='insercion'),
    path('editarinsercion/<pk>/', InsercionEditView.as_view(), name='editar-insercion'),
    path('contrato/', FormContratoView.as_view(), name='contrato'),
    path('editarcontrato/<pk>/', ContratoEditView.as_view(), name='editar-contrato'),
    path('usuario/', UserView.as_view(), name='user'),
    path('pdfInsercion/<pk>/', pdfInsercion, name='pdf-incersion'),
    path('pdfContrato/<pk>/', pdfContrato, name='pdf-contrato'),
    # path('signup/', add_user_logout_view, name="signup"),
    path('search/', search, name="search")
]

