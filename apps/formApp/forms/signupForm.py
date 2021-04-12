from django import forms
from django.contrib.auth import get_user_model

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['nombre_Razon_Social', 'nro_IDentificación_Fiscal_NIF', 'direccion', 'codigo_postal', 'phone']

        labels = {
            'nombre_Razon_Social' : 'Nombre o Razón Social',
            'nro_IDentificación_Fiscal_NIF' : 'Número de Identificación Fiscal NIF',
            'direccion' : 'Dirección',
            'codigo_postal' : 'Código Postal',
            'phone' : 'Teléfono',
        }

        widgets = {
            'nombre_Razon_Social': forms.TextInput(attrs={'placeholder':'', 'class': 'form-control'}),
            'nro_IDentificación_Fiscal_NIF': forms.TextInput(attrs={'placeholder':'', 'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'placeholder':'', 'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'placeholder':'', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder':'', 'class': 'form-control'})
        }

    def signup(self, request, user):
        user.phone = self.cleaned_data['phone']
        user.nombre_Razon_Social = self.cleaned_data['nombre_Razon_Social']
        user.nro_IDentificación_Fiscal_NIF = self.cleaned_data['nro_IDentificación_Fiscal_NIF']
        user.direccion = self.cleaned_data['direccion']
        user.codigo_postal = self.cleaned_data['codigo_postal']
        user.save()