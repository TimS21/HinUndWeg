from django.shortcuts import render

from .models import Vehicles

# Create your views here.
def main(request):
    return render(request, 'landingpage.html')
def detailpage(request):
    obj = Vehicles.objects.get(id = 1)
    context = {
        "object":obj
    }
    return render(request, 'detailpage.html', context)
