from django.shortcuts import render

from .models import Vehicles
from .models import User


# Create your views here.
def main(request):
    return render(request, 'landingpage.html')

def detailpage(request):
    if request.GET.get("Bike") == "Bike":
        obj = Vehicles.objects.get(id = 1)
    elif request.GET.get("Roller") == "Roller":
        obj = Vehicles.objects.get(id = 2)
    elif request.GET.get("Scooter") == "Scooter":
        obj = Vehicles.objects.get(id = 3)

    context = {
        "object":obj
    }
    return render(request, 'detailpage.html', context)

def bookingpage(request):
    if request.method == "POST":
        vName = request.POST["vname"]
        nName = request.POST["nname"]
        eMail = request.POST["email"]
        telNr = request.POST["telnr"]

        new_user = User(vname=vName, nname=nName, eMail=eMail, telNr=telNr)
        new_user.save()


    return render(request, 'bookingpage.html')

def confirmationpage(request):
    return render(request, 'confirm.html')
