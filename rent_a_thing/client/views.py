from rest_framework import viewsets
from django.shortcuts import render
from core.models import Rental
from client.serializers import ClientConfigSerializer
from client.models import ClientReservation

# Create your views here.

class ClientReservationViewSet(viewsets.ViewSet):
    queryset = ClientReservation.objects.all()
    serializer_class = ClientReservationSerializer
