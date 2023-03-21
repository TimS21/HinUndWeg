from django.forms import ModelForm
from django import forms
from main.models import User

class UploadForm(ModelForm):
    Vorname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    Nachname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    EMailAdresse = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    telNr = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['Vorname', 'Nachname', 'EMailAdresse', 'telNr']
    
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)