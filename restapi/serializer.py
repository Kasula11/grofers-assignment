from rest_framework import serializers
from .models import Capacity
from .models import Availability
from .models import VehiclesPerDay
from .models import VehicleType

class CapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacity
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class VehiclesPerDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclesPerDay
        fields = '__all__'

