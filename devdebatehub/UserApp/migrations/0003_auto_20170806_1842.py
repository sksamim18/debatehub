# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_auto_20170805_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='activityfollow',
        ),
        migrations.AddField(
            model_name='person',
            name='details',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]