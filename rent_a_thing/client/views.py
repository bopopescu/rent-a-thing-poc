from django.shortcuts import render
from core.models import Rental
from rest_framework.views import APIView
from client.serializers import ClientConfigSerializer, ClientReservationSerializer
from client.models import ClientReservation
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ClientReservationList(APIView):

    """
    List all client reservations, or create a new client reservation.
    """
    def get(self, request, format=None):
        snippets = ClientReservation.objects.all()
        serializer = ClientReservationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        