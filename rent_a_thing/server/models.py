from django.db import models

# Create your models here.

class Clients(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeFIeld(auto_now=True)
    description = models.CharField(max_length=150, blank=False)
    Address = models.CharField(max_length=500, blank=False)
    HostAddress = models.CharField(max_length=150, blank=False)
