from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from server.serializers import ClientSerializer
from server.models import Client
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @csrf_exempt
    def list_all(self, request):
        if request.method == 'GET':
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return JsonResponse(serializer.data, safe=False)