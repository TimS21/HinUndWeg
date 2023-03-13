from django.shortcuts import redirect, render

from hinUndWeg.forms import *

from .models import *


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
    return render(request, 'bookingpage.html')

def confirmationpage(request):
    return render(request, 'confirm.html')

def uploadData(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect(overview)
    return render(request, 'bookingpage.html', {'form' : UploadForm})

def imprint(request):
    return render(request, 'imprint.html')

def overview(request):
    if request.GET.ORT("DHBW") == "DHBW":
        obj = Vehicles.objects.get(standort = "DHBW")
    elif request.GET.ORT("HBF") == "HBF":
        obj = Vehicles.objects.get(standort = "Bahnhof")
    elif request.GET.ORT("WTM") == "WTM":
        obj = Vehicles.objects.get(standort = "Wasserturm")
    context = {
        "object":obj
    }
    return render(request, 'overview.html', context)

