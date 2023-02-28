from django.db import models

# Create your models here.

class Vehicles(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=30)
    preisProTag = models.IntegerField(default=15)



