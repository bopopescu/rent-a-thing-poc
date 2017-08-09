from django.contrib import admin
from core.models import RentalObject, Rental, Client

# Register your models here.

admin.site.register(RentalObject)
admin.site.register(Rental)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('description', 'address', 'host_address', 'created', 'last_update')
    fields = ('description', 'address', 'host_address')
    ordering = ('last_update', '-created',)

admin.site.register(Client, ClientAdmin)
