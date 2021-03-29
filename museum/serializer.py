from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class MuseumSerializer(serializers.ModelSerializer):


    class Meta:
        model = Museum
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['trip','date','price']


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ['name','date','places','museum']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['name','age','wallet','email','phone']


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    count_place = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['ticket','date_created','status','profile','quantity','total_price','count_place']


    def get_total_price(self,obj):
        total_price = 0
        try:
            total_price += obj.quantity * obj.ticket.price
            obj.total_sum = total_price
            obj.save()
            return total_price
        except AttributeError:
            return 0



    def get_count_place(self, obj):
        try:
            obj.ticket.trip.places -= obj.quantity
            obj.ticket.trip.save()

        except IntegrityError:
            raise ValidationError("NO PLACES!")







