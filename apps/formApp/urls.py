from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    FormContrato,
)

app_name = 'core'

urlpatterns = [
    path('form/', FormContrato.as_view(), name='formContrato'),
    path('', FormContrato.as_view(), name='index'),
]

