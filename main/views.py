from django.shortcuts import redirect, render

from hinUndWeg.forms import *

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
    return render(request, 'bookingpage.html')

def confirmationpage(request):
    return render(request, 'confirm.html')

def uploadData(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect(confirmationpage)
    return render(request, 'bookingpage.html', {'form' : UploadForm})

def imprint(request):
    return render(request, 'imprint.html')

