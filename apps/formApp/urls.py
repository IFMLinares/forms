from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    test
)

app_name = 'core'

urlpatterns = [
    path('', test, name='test'),
]

