from django.contrib import admin
from core.models import RentalObject, Rental, Client

class RentalObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_tenant', 'last_update', 'created')
    fields = ['id', 'current_tenant']
    readonly_fields = ['id']
    ordering = ('last_update', '-created',)

class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant_user', 'rented_object', 'is_confirmed', 'rental_station')
    fields = ['id', 'tenant_user', 'rented_object', 'is_confirmed', 'rental_station', 'return_station', 'last_update', 'created']
    readonly_fields = ['id', 'tenant_user', 'rented_object', 'is_confirmed', 'rental_station', 'return_station', 'last_update', 'created']
    ordering = ('last_update', '-created')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('description', 'address', 'host_address', 'created', 'last_update')
    fields = ('description', 'address', 'host_address')
    ordering = ('last_update', '-created',)

admin.site.register(Client, ClientAdmin)
admin.site.register(RentalObject, RentalObjectAdmin)
admin.site.register(Rental, RentalAdmin)