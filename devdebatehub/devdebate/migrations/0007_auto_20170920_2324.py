# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devdebate', '0006_opinion_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='opinionby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opinion_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
