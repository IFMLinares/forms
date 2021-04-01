from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    Index,
)

app_name = 'core'

urlpatterns = [
    path('', Index.as_view(), name='index'),
]

