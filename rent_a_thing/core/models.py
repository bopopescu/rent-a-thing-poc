import uuid
from django.contrib.auth.models import User
from django.db import models
from server.models import Client
# Create your models here.

class RentalObject (models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    current_tenant_user = models.OneToOneField(User, on_delete=models.PROTECT)
    
class Rental (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tenant_user = models.OneToOneField(User, on_delete=models.PROTECT)
    rented_object = models.OneToOneField(RentalObject, on_delete=models.PROTECT)
    is_confirmed = models.BooleanField(default=True)
    rental_station = models.OneToOneField(Client, on_delete=models.PROTECT)
    return_station = models.OneToOneField(Client, on_delete=models.PROTECT)
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()
    