from django.db import models

# Create your models here.

class Type(models.Model):
    BIKE = "EB"
    SCOOTER = "ES"
    ROLLER = "ER"
    TYPE_OF_VEHICLE_CHOICES = [
        (BIKE, "E-BIKE"),
        (SCOOTER, "E-Scooter"),
        (ROLLER, "E-Roller")
    ]
    type = models.CharField(max_length=2, choices=TYPE_OF_VEHICLE_CHOICES, default=BIKE)

class Vehicles(models.Model):
    vid = models.IntegerField(auto_created=True, primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)




class User(models.Model):
    vName = models.CharField(max_length=30, null=False, blank=False)
    nName = models.CharField(max_length=30, null=False, blank=False)
    eMail = models.EmailField(default="test@gmail.com")
    telNr = models.IntegerField(default=1234)




