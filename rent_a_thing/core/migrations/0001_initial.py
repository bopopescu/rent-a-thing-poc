# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 02:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=500)),
                ('host_address', models.CharField(max_length=150)),
                ('identifier', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('is_confirmed', models.BooleanField(default=True)),
                ('rental_date', models.DateTimeField(blank=True)),
                ('return_date', models.DateTimeField(blank=True)),
                ('rental_station', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='rental_client_station', to='core.Client')),
            ],
        ),
        migrations.CreateModel(
            name='RentalObject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('current_tenant', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='rental',
            name='rented_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.RentalObject'),
        ),
        migrations.AddField(
            model_name='rental',
            name='return_station',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='return_client_station', to='core.Client'),
        ),
        migrations.AddField(
            model_name='rental',
            name='tenant_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='available_objects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.RentalObject'),
        ),
    ]