import uuid
from django.contrib.auth.models import User
from django.db import models

class RentalObject (models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tenant_user = models.OneToOneField(User, on_delete=models.PROTECT)
    