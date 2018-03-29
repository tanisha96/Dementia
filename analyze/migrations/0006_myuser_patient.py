# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-27 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyze', '0005_auto_20180327_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10, null=True)),
                ('lname', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('userid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_fname', models.CharField(max_length=10, null=True)),
                ('patient_lname', models.CharField(max_length=10, null=True)),
                ('patient_address', models.CharField(max_length=10, null=True)),
                ('patient_email', models.CharField(max_length=100, null=True)),
                ('pid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
