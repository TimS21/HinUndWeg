from django.contrib import admin
from .models import Vehicles
from .models import User

# Register your models here.

admin.site.register(Vehicles)
admin.site.register(User)
