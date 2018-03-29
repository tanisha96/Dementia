from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    patient_id=models.IntegerField(primary_key=True)
    patient_fname = models.CharField(max_length=10, null=True)
    patient_lname = models.CharField(max_length=10, null=True)
    patient_address = models.CharField(max_length=10, null=True)
    patient_email = models.CharField(max_length=100, null=True)


class data1(models.Model):
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)
    alpha=models.FloatField(max_length=250)
    beta=models.FloatField(max_length=250)
    theta=models.FloatField(max_length=250)
    delta=models.FloatField(max_length=250)
    slow_flag=models.FloatField(max_length=250)
    slowing=models.CharField(max_length=250)


class data2(models.Model):
    slowing = models.FloatField(max_length=250)
    age = models.FloatField(max_length=250)
    memory = models.FloatField(max_length=250)
    interpretation = models.FloatField(max_length=250)
    muffled = models.FloatField(max_length=250)
    behaviour = models.FloatField(max_length=250)
    visual = models.FloatField(max_length=250)
    chances = models.FloatField(max_length=250)

class undata2(models.Model):
    slowing = models.FloatField(max_length=250)
    age = models.FloatField(max_length=250)
    memory = models.FloatField(max_length=250)
    interpretation = models.FloatField(max_length=250)
    muffled = models.FloatField(max_length=250)
    behaviour = models.FloatField(max_length=250)
    visual = models.FloatField(max_length=250)
    chances = models.FloatField(max_length=250)
    flag = models.IntegerField(max_length=250,null=True)

class Myuser(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    fname = models.CharField(max_length=10, null=True)
    lname = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.fname)



