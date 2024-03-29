from datetime import timezone
import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Type(models.Model):
    BIKE = "E-Bike"
    SCOOTER = "E-Scooter"
    ROLLER = "E-Roller"
    TYPE_OF_VEHICLE_CHOICES = [
        (BIKE, "E-BIKE"),
        (SCOOTER, "E-Scooter"),
        (ROLLER, "E-Roller")
    ]
    BP = "9"
    SP = "6"
    RP = "18"
    PRICE_OF_TYPE = [
        (BP, "Bike Price"),
        (SP, "Scooter Price"),
        (RP, "Roller Price")
    ]
    type = models.CharField(max_length=9, choices=TYPE_OF_VEHICLE_CHOICES, default=BIKE, primary_key=True)
    price = models.CharField(max_length=2, choices=PRICE_OF_TYPE, default=BP)
    power = models.CharField(max_length=2, default="1")
    distance = models.CharField(max_length=3, default="100")
    weight = models.CharField(max_length=3, default="10")
    wheelsize = models.CharField(max_length=2, default="24")
    Beschreibung = models.TextField(default="Hier steht die Beschreibung")
    image = models.ImageField (upload_to='main\static\images\detailpage', default="e-Bike.jpg")

    def __str__(self):
        return self.type

class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uid) + " " + str(self.user)



class Location(models.Model):
    lid = models.IntegerField(primary_key=True)
    bezeichnung = models.CharField(max_length=21)
    strasse = models.CharField(max_length=50)
    nummer = models.IntegerField(null=False)
    plz = models.IntegerField()
    ort = models.CharField(max_length=30)

    def __str__(self):
        return self.bezeichnung


class Vehicles(models.Model):
    vid = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default="1")
    lid = models.ForeignKey(Location, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return str(self.vid) + ' ' + str(self.type)
    
    
class Buchungstabelle(models.Model):
    bid = models.IntegerField(primary_key=True, default=0)
    vid = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    tstart = models.DateField()
    tend = models.DateField()

    def __str__(self):
        return 'Buchungsnummer: ' + str(self.bid)
