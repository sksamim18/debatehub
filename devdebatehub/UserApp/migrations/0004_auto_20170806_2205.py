# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_auto_20170806_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='birthlocation',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='person',
            name='currentlocation',
        ),
    ]
