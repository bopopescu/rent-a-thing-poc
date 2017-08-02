from django.contrib import admin
from server.models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('description', 'address', 'host_address', 'created', 'last_update')
    fields = ('description', 'address', 'host_address')
    ordering = ('last_update', '-created',)

admin.site.register(Client, ClientAdmin)
