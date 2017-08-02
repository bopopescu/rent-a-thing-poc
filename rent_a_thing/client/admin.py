from django.contrib import admin
from client.models import ClientConfig, ClientReservation

# Register your models here.

admin.site.register(ClientConfig)
admin.site.register(ClientReservation)