from django.db import models

class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #email = models.EmailField(max_length=254)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    gender = models.BooleanField(default=False)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    gender = models.BooleanField()
    email = models.EmailField(max_length=254)
    position = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

class Laundry(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

class Order(models.Model):
    laundry = models.ForeignKey(Laundry, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_ordered = models.DateField()
    time_pickup = models.TimeField()
    delivery_date = models.DateField(default="2019-04-11", null=True)
    delivery_time = models.TimeField(null=True)
    is_selfpickup = models.BooleanField()
    status = models.IntegerField()
    price = models.IntegerField()
    is_paid = models.BooleanField()
    date_payment = models.DateField(null=True)

class ItemToOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prive = models.IntegerField()

class CourierToOrder(models.Model):
    courier = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    is_pickpup = models.BooleanField()
