from django.db import models

# Create your models here.

class ClientConfig(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    identifier = models.UUIDField(editable=True, blank=False)

    class Meta:
        ordering = ('created',) 