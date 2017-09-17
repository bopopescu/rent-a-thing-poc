from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import RentalObject, Rental, Client, Profile

class RentalObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_tenant', 'current_station', 'last_update', 'created')
    fields = ['id', 'current_tenant', 'current_station']
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

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    readonly_fields = ['last_login', 'date_joined']
    inlines = [ProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(RentalObject, RentalObjectAdmin)
admin.site.register(Rental, RentalAdmin)