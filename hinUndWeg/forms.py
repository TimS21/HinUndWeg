from django.forms import ModelForm
from django import forms
from main.models import User

class UploadForm(ModelForm):
    Vorname = forms.TextInput()
    Nachname = forms.TextInput()
    EMailAdresse = forms.EmailInput()
    telNr = forms.IntegerField()
    class Meta:
        model = User
        fields = ['Vorname', 'Nachname', 'EMailAdresse', 'telNr']