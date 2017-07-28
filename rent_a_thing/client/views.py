from django.shortcuts import render
from core.models import Rental
from rest_framework import generics
from client.serializers import ClientConfigSerializer, ClientReservationSerializer
from client.models import ClientReservation
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class ClientReservationViewSet(viewsets.ModelViewSet):
    queryset = ClientReservation.objects.all()
    serializer_class = ClientReservationSerializer
