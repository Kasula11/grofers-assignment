from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Capacity)
admin.site.register(Availability)
admin.site.register(VehiclesPerDay)
admin.site.register(VehicleType)