# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devdebate', '0008_auto_20170921_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opinion',
            options={'ordering': ['-legit', '-id']},
        ),
        migrations.AlterField(
            model_name='debate',
            name='stat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='description',
            field=models.CharField(max_length=100000),
        ),
    ]