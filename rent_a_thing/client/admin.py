from django.contrib import admin
from client.models import ClientConfig

# Register your models here.

class ClientConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'identifier', 'last_update', 'created')
    fields = ['id', 'created', 'last_update', 'identifier']
    readonly_fields = ['id', 'created', 'last_update', 'identifier']
    ordering = ('last_update', '-created',)

admin.site.register(ClientConfig, ClientConfigAdmin)