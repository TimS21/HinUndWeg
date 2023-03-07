from django.forms import ModelForm
from django import forms
from main.models import User

class UploadForm(ModelForm):
    vName = forms.TextInput()
    nName = forms.TextInput()
    eMail = forms.EmailInput()
    telNr = forms.IntegerField()
    class Meta:
        model = User
        fields = ['vName', 'nName', 'eMail', 'telNr']