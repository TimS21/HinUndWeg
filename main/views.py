from django.shortcuts import render

from .models import Vehicles
from .models import User
from .models import Type


# Create your views here.
def main(request):
    return render(request, 'landingpage.html')

def detailpage(request):
    if request.GET.get("Bike") == "Bike":
        obj = Type.objects.get(weight = 25)
    elif request.GET.get("Roller") == "Roller":
        obj = Type.objects.get(weight = 120)
    elif request.GET.get("Scooter") == "Scooter":
        obj = Type.objects.get(weight = 15)

    context = {
        "object":obj
    }
    return render(request, 'detailpage.html', context)

def bookingpage(request):
    if request.method == "POST":
        Vorname = request.POST["Vorname"]
        Nachname = request.POST["Nachname"]
        eMail = request.POST["email"]
        telNr = request.POST["telnr"]

        new_user = User(Vorname=Vorname, Nachname=Nachname, eMail=eMail, telNr=telNr)
        new_user.save()


    return render(request, 'bookingpage.html')

def confirmationpage(request):
    return render(request, 'confirm.html')
def imprint(request):
    return render(request, 'imprint.html')
