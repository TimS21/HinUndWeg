from django.shortcuts import redirect, render
from django.http import HttpResponse

from hinUndWeg.forms import *

from .models import *


# Create your views here.
def main(request):
    return render(request, 'landingpage.html')

def detailpage(request):
    bezeichnungen = Location.objects.all

    if request.GET.get("Bike") == "Bike":
        obj = Type.objects.get(weight = 25)
        img = 1
    elif request.GET.get("Roller") == "Roller":
        obj = Type.objects.get(weight = 120)
        img = 2
    elif request.GET.get("Scooter") == "Scooter":
        obj = Type.objects.get(weight = 15)
        img = 3

    context = {
        "object":obj,
        "image":img,
        "bez":bezeichnungen
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
    return render(request, 'overview.html')

    

