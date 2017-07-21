from django.shortcuts import render
from core.models import Rental
from rest_framework import generics
from client.serializers import ClientConfigSerializer, ClientReservationSerializer
from client.models import ClientReservation
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ClientReservationList(generics.ListCreateAPIView):
    queryset = ClientReservation.objects.all()
    serializer_class = ClientReservationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)