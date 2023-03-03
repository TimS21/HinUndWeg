from django.db import models

# Create your models here.

class Vehicles(models.Model):
    id = models.IntegerField(auto_created=False, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30, null=False, blank=False)
    preisProTag = models.IntegerField(default=20)

class User(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    vName = models.CharField(max_length=30, null=False, blank=False)
    nName = models.CharField(max_length=30, null=False, blank=False)
    eMail = models.EmailField(default="test@gmail.com")
    telNr = models.IntegerField(default=1234)




