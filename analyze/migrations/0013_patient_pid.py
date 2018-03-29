# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-28 04:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyze', '0012_remove_patient_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
