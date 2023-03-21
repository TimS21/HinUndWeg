from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    vorname = forms.CharField(max_length = 50)
    nachname = forms.CharField(max_length = 50)

    class Meta:
        model = User
        fields = ('username', 'vorname', 'nachname',  'email', 'password1', 'password2')