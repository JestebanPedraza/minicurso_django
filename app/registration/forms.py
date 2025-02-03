from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # widgets = {}

    # Función para eliminar los textos ayuda
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields:
    #         self.fields[field_name].help_text = ''


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
