from rest_framework import serializers

from .models import *


class MuseumSerializer(serializers.ModelSerializer):


    class Meta:
        model = Museum
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['date','price','trip']


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ['name','date','places','museum']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['name','age','wallet','email','phone']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['ticket','date_created','status','profile','quantity']