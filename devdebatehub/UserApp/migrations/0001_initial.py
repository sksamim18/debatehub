# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 18:23
from __future__ import unicode_literals

import UserApp.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowingUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=UserApp.models.get_org_pic_path)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'orgs',
                'verbose_name': 'org',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=30)),
                ('lastname', models.CharField(blank=True, max_length=30)),
                ('birthlocation', models.CharField(blank=True, max_length=30)),
                ('currentlocation', models.CharField(blank=True, max_length=30)),
                ('school', models.CharField(blank=True, max_length=30)),
                ('collage', models.CharField(blank=True, max_length=30)),
                ('interestedin', models.CharField(blank=True, max_length=100)),
                ('profileimage', models.ImageField(blank=True, null=True, upload_to=UserApp.models.get_person_pic_path)),
            ],
            options={
                'verbose_name_plural': 'persons',
                'verbose_name': 'person',
            },
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=30, unique=True)),
                ('usertype', models.CharField(blank=True, choices=[('university', 'University'), ('school', 'School'), ('companies', 'Companies'), ('media', 'Media'), ('ngo', 'NGO')], max_length=50, null=True)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organisation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followinguser',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followinguser',
            name='following',
            field=models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
