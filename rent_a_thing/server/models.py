import uuid
from django.db import models

# Create your models here.

class Client(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=500, blank=False)
    host_address = models.CharField(max_length=150, blank=False)
    identifier = models.UUIDField(default=uuid.uuid4, editable=True, blank=False)

    class Meta:
        ordering = ('created',)
