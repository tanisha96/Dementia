# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-28 04:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0013_patient_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='pid',
        ),
    ]
