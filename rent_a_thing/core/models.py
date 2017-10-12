import uuid
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Price(models.Model):
    value = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=20)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(null=False, blank=False, max_length=14, unique=True)
    address1 = models.CharField(default='', blank=True, max_length=150)
    address2 = models.CharField(default='', blank=True, max_length=150)
    zipcode = models.CharField(default='', blank=True, max_length=9)

class Client(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=500, blank=False)
    host_address = models.CharField(max_length=150, blank=False)
    identifier = models.UUIDField(default=uuid.uuid4, editable=True, blank=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('created',)

class RentalObject (models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    current_tenant = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    current_station = models.ForeignKey(Client, related_name='rental_objects', blank=True, null=True)
    station_id = models.IntegerField(blank=True, null=True)
    is_return = models.NullBooleanField(blank=True, null=True)
    rental_cost = models.IntegerField(blank=True, null=True)


class Rental (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tenant_user = models.OneToOneField(User, on_delete=models.PROTECT)
    rented_object = models.OneToOneField(RentalObject, on_delete=models.PROTECT)
    rental_station = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='rental_client_station', blank=True)
    return_station = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='return_client_station', null=True, blank=True)
    rental_date = models.DateTimeField(blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

class Wallet (models.Model):
    last_update = models.DateTimeField(auto_now=True)
    id = models.OneToOneField(User, primary_key=True)
    balance = models.BigIntegerField(blank= True, null=True, default=0)

class Transaction (models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add= True)
    last_update = models.DateTimeField(auto_now=True)
    amount_paid = models.DecimalField(max_digits=24, decimal_places=2)
    credits_purchased = models.BigIntegerField(blank=True, null=True)
    price_per_credit = models.DecimalField(max_digits=24, decimal_places=2)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    transaction_code = models.CharField(unique=True, max_length=36, null=True)
