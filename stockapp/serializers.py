from rest_framework import serializers
from .models import *


class WarehouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'location']


class ProductSerializers(serializers.ModelSerializer):
    total_amout = serializers.ReadOnlyField()
    sales_price = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ('user', 'warehouse', 'name', 'price', 'quantity', 'sku', 'date', 'total_amout', 'sales_price')

    

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ShimpentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
    