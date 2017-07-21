import uuid
from django.contrib.auth.models import User
from django.db import models
from server.models import Client
# Create your models here.

class RentalObject (models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    current_tenant = models.OneToOneField(User, on_delete=models.PROTECT)
    
class Rental (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tenant_user = models.OneToOneField(User, on_delete=models.PROTECT)
    rented_object = models.OneToOneField(RentalObject, on_delete=models.PROTECT)
    is_confirmed = models.BooleanField(default=True)
    rental_station = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='rental_client_station', blank=True)
    return_station = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='return_client_station', blank=True)
    rental_date = models.DateTimeField(blank=True)
    return_date = models.DateTimeField(blank=True)
