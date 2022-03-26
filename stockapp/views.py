from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *


class WarehouseAPIView(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializers

class WarehouseCreateAPIView(generics.CreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializers

class WarehouseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializers

class WarehouseRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializers


# *******************************************

def tables(request):
    return render(request, 'stockapp/tabels.html')

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

# *******************************************


class CustomerAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class CustomerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


# *******************************************


class ShipmentAPIView(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShimpentSerializers

class ShipmentCreateAPIView(generics.CreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShimpentSerializers

class ShipmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShimpentSerializers

class ShipmentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShimpentSerializers

