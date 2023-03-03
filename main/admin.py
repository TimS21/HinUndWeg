from django.contrib import admin
from .models import Vehicles
from .models import User
from .models import Type
from .models import Buchungstabelle

# Register your models here.

admin.site.register(Vehicles)
admin.site.register(User)
admin.site.register(Type)
admin.site.register(Buchungstabelle)
