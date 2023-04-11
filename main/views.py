from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail
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


def uploadData(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect(overview)
    
    if request.GET.get("Dhbw") == "Dhbw":
        map = 1
    elif request.GET.get("Hbf") == "Hbf":
        map = 2
    elif request.GET.get("Wt") == "Wt":
        map = 3
    
    context = {
        "map":map,
        "form":UploadForm
    }
    return render(request, 'bookingpage.html', context)

def confirmationpage(request):
    return render(request, 'confirm.html')

def imprint(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # email senden
        send_mail(
            'Nachricht von ' + message_name, # Titel der Mail
            message, # Nachricht
            message_email, # Sender
            ['tim.schefczik@gmail.com'], # Empfänger           
        )

        return render(request, 'imprint.html', {'message_name': message_name})

    else:
        return render(request, 'imprint.html', {})

def overview(request):
    anzahl = int(request.GET['anzahl'])
    price = int(request.GET['price'])
    tage = int(request.GET['tage'])
    gesamt = anzahl*price*tage

    datum = int(request.GET['Date'])
    datum2 = int(request.GET['Date2'])
    dGes = datum2-datum

    if request.GET.get("Dhbw") == "Dhbw":
        map = 1
        Text = "DHBW-Mannheim"
    elif request.GET.get("Hbf") == "Hbf":
        map = 2
        Text = "Hauptbahnhof"
    elif request.GET.get("Wt") == "Wt":
        map = 3
        Text = "Wasserturm"

    context = {
        "map":map,
        "text":Text,
        "gesamt":gesamt,
        "datum":dGes

    }
    return render(request, 'overview.html', context)

    

