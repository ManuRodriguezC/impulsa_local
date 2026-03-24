from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    is_entrepreneur = forms.BooleanField(
        required=False,
        label="Registrarse como emprendedor"
    )

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'document',
            'phone',
            'address',
            'password1',
            'password2'
        ]