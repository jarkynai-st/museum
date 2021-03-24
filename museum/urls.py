from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [

    path('museum/',MuseumView.as_view()),
    path('ticket/',TicketView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('trip/<int:trip_id>/',TicketView.as_view()),
    path('trip/',TripView.as_view()),
    path('order/',OrderAPIView.as_view()),

]