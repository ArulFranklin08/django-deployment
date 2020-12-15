#!/usr/bin/env python
from django.db import models

# Create your models here.
class Tracking(models.Model):
    sno = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    phone_no = models.IntegerField(null=True)


    def __str__(self):
        return self.phone_no
