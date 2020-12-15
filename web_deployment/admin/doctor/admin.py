#!/usr/bin/env python
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Doctor_listAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','speciality','email','mobile_no','doctor_image']
    list_filter = ['doctor_name']
