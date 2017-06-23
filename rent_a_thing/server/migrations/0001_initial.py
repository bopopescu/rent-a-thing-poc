# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
