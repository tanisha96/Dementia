# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-26 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha', models.FloatField(max_length=250)),
                ('beta', models.FloatField(max_length=250)),
                ('theta', models.FloatField(max_length=250)),
                ('delta', models.FloatField(max_length=250)),
                ('slow_flag', models.FloatField(max_length=250)),
                ('slowing', models.CharField(max_length=250)),
            ],
        ),
    ]
