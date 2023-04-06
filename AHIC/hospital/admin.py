from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(hosp_details)
admin.site.register(hospital)
admin.site.register(HospNotification)

