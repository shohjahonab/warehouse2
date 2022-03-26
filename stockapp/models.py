import uuid
from django.db import models
from django.conf import settings




class Warehouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Ware house', max_length=255, blank=False, null=False)
    location = models.CharField(verbose_name='Ware location', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Product name', max_length=255)
    price = models.DecimalField(verbose_name='Unit Price', decimal_places=2, max_digits=9)
    quantity = models.PositiveIntegerField('Product quantity',)
    sku = models.CharField(verbose_name='Stock Keeping Unit', blank=True, null=True, max_length=50)
    date = models.DateField(verbose_name='Product adding date', auto_now=True)

    def __str__(self):
        return self.name

    def total_amout(self):
        return self.quantity * self.price


    def sales_price(self):
        persentage = self.price / 100
        profit = persentage * 15
        return self.price + profit


class Customer(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Shipment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    destination = models.CharField(verbose_name='Product Shipment Destination', max_length=255)
    quantity = models.PositiveIntegerField('Shipmet Product Quantity ')

    def __str__(self):
        return f'Shipment #{self.id}'


