from rest_framework import viewsets
from django.shortcuts import render
from core.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from core.permissions import WriteOnly

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = None
    permission_classes = (WriteOnly,)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None