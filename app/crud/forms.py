from django import forms
from core.models import Cliente


class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'cedula', 'email']
