from django.db import models
from django.contrib.auth.models import User
from core.models import RentalObject

# Create your models here.

class ClientConfig(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    identifier = models.UUIDField(editable=True, blank=False)

    class Meta:
        ordering = ('created',) 

class ClientReservation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tenant_user = models.OneToOneField(User, on_delete=models.PROTECT)
    rental_object = models.OneToOneField(RentalObject, on_delete=models.PROTECT)
