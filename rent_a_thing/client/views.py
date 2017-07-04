from rest_framework import viewsets
from django.shortcuts import render
from client.models import ClientConfig
from client.serializers import ClientConfigSerializer

# Create your views here.

class CommandViewSet(viewsets.ViewSet):
    queryset = ClientConfig.objects.all()
    serializer_class = ClientConfigSerializer


