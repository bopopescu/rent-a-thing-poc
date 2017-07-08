from rest_framework import viewsets
from django.shortcuts import render
from core.models import Rental
from client.serializers import ClientConfigSerializer

# Create your views here.

class CommandViewSet(viewsets.ViewSet):
    queryset = Rental.objects.all()
    serializer_class = ClientConfigSerializer
