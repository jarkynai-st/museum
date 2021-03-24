from django.db import models

# Create your models here.


class Museum(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    status = models.CharField(max_length=20)


class Ticket(models.Model):
    trip = models.ForeignKey('Trip',on_delete=models.SET_NULL,null=True,related_name='tickets')
    date = models.DateField()
    price = models.PositiveIntegerField(default=0)


class Trip(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    places = models.PositiveIntegerField(default=0)
    museum = models.ForeignKey('Museum',on_delete=models.SET_NULL,null=True,related_name='trips')


class Profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    wallet = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    phone = models.IntegerField()


class Order(models.Model):
    statuses = (
        ('pending', 'pending'),
        ('finished', 'finished'),
    )
    ticket = models.ForeignKey('Ticket',on_delete=models.SET_NULL,null=True,related_name='orders')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=statuses,max_length=20,default='pending')
    quantity = models.PositiveIntegerField()
    profile = models.ForeignKey('Profile',on_delete=models.SET_NULL,null=True,related_name='orders')

