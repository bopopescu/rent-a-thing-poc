# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 02:35
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='identifier',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
