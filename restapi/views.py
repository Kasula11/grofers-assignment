from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Capacity
from .models import Availability
from .models import VehiclesPerDay
from .models import VehicleType
from .serializer import Availability
from .serializer import VehiclesPerDay
from .serializer import Capacity
from .serializer import VehicleType
import json
import heapq

def get_max_vehicles_we_can_use_per_a_day(vehicle_id):
    vehicle = VehiclesPerDay.objects.get(vehicle_id=vehicle_id)
    return vehicle.vehicle_count_per_day

def get_vehicle_capacity(vehicle_id): 
    capacity = Capacity.objects.get(vehicle_id=vehicle_id)
    return capacity.vehicle_capacity

def get_vehicle_type(vehicle_id):
    vehicle_type = VehicleType.objects.get(vehicle_id=vehicle_id) 
    return vehicle_type.vehicle_type

def get_vehicle_details(vehicle_availability):
    vehicle_details = []
    for vehicle_id in vehicle_availability:
        vehicle_capacity = get_vehicle_capacity(vehicle_id)
        vehicle_type = get_vehicle_type(vehicle_id)
        vehicle_count_per_day = get_max_vehicles_we_can_use_per_a_day(vehicle_id) 
        heapq.heappush(vehicle_details, (vehicle_capacity, vehicle_id, vehicle_type, vehicle_count_per_day))
    return vehicle_details

def get_order_details(orders):
    order_details = []
    for order in orders:
        order_id = int(order['order_id'])
        order_weight = int(order['order_weight'])
        heapq.heappush(order_details, (order_weight, order_id))
    return order_details

def get_vehicles_available_in_particular_slot(slot_id):
    available = Availability.objects.get(slot_id=slot_id)
    vehicle_ids_available = available.vehicle_availability
    available_vehicles = vehicle_ids_available.replace('[','').replace(']','').split(',')
    return available_vehicles   

def allocate_orders(orders, slot_id):
    allocate_orders = []
    vehicles_available = get_vehicles_available_in_particular_slot(slot_id)
    order_details = get_order_details(orders)
    vehicle_details = get_vehicle_details(vehicles_available)
    count = 1
    while vehicle_details:
        vehicle = heapq.heappop(vehicle_details)
        if vehicle[3] > 0:
            heapq.heappush(vehicle_details, (vehicle[0], vehicle[1], vehicle[2], vehicle[3] - 1))
        capacity = vehicle[0]
        orders_for_vehicle = []
        while order_details and capacity - heapq.nsmallest(1, order_details)[0][0] >= 0:
            order = heapq.heappop(order_details)
            weight = order[0]
            orders_for_vehicle.append(order[1])
            capacity = capacity - weight 

        if len(orders_for_vehicle) > 0:
            allocate_orders.append({'vehicle_type':vehicle[2],'delivery_partner_id':count,'list_order_ids_assigned':orders_for_vehicle})
            count += 1
    return allocate_orders



@api_view(['POST'])
def get_orders(request, pk):
    recieved_json = json.loads(request.body.decode('utf-8'))
    allocated_orders = allocate_orders(recieved_json['orders'], pk)
    return JsonResponse(allocated_orders,safe=False) 
