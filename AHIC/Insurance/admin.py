from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Bank)
admin.site.register(BankInsurance)
admin.site.register(UserDetails)
admin.site.register(Billing)