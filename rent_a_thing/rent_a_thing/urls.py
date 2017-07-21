"""rent_a_thing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from server import views as server_views
from client import views as client_views
from core import views as core_views

core_router = routers.DefaultRouter()
core_router.register(r'users', core_views.UserViewSet)
core_router.register(r'groups', core_views.GroupViewSet)

server_router = routers.DefaultRouter()
server_router.register(r'clients', server_views.ClientViewSet)

client_router = routers.DefaultRouter()
client_router.register(r'reservations', client_views.ClientReservationViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^server/api/', include(server_router.urls)),
    url(r'^client/api/', include(client_router.urls)),
    url(r'^core/api/', include(core_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
