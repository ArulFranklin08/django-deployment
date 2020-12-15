#!/usr/bin/env python
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Doctor_list(models.Model):
    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField(null=True)
    email = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=20, null=True)
    doctor_image = models.ImageField(blank=True,upload_to='images/')
    doctor_image_url = models.CharField(max_length=20, null=True)
    doctor_alt_image = models.CharField(max_length=20, null=True)
    discount = models.IntegerField(null=True)
    street_name = models.CharField(max_length=100, null=True)
    distance = models.CharField(max_length=100, null=True)

   
