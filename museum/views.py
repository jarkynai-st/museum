from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializer import MuseumSerializer, TicketSerializer, TripSerializer, ProfileSerializer, OrderSerializer


class MuseumView(views.APIView):

    def get(self,request,*args,**kwargs):
        museum = Museum.objects.all()
        serializer = MuseumSerializer(museum,many=True)
        return Response(serializer.data)


class TicketView(views.APIView):
    def get(self,request,*args,**kwargs):
        trip = Trip.objects.get(id=kwargs['trip_id'])
        serializer = TripSerializer(trip)
        return Response(serializer.data)


class TripView(views.APIView):
    def get(self,request,*args,**kwargs):
        trip = Trip.objects.all()
        serializer = TripSerializer(trip,many=True)
        return Response(serializer.data)


class ProfileView(views.APIView):
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)


class OrderAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response({
                    "id": 1,
                    "user":1,
                    "ticket":1,
                    "museum":2,
                    "quantity":5,
                    "date_created": "2021-03-24T17:49:28.748633+06:00",
                    "status": "pending"
                        })

    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
