from django.db import models

# Create your models here.
class Capacity(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_capacity = models.IntegerField()

class Availability(models.Model):
    slot_id = models.IntegerField(primary_key=True)
    vehicle_availability = models.CharField(max_length=1000)


class VehicleType(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_type = models.CharField(max_length=900)


class VehiclesPerDay(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_type = models.CharField(max_length=900)
    vehicle_count_per_day = models.IntegerField()