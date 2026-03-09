from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    # eredita ed estende UserCreationForm
    email = forms.EmailField(required=True) # va aggiunta perchè UserCreationForm definisce solo username e password1, password2

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")