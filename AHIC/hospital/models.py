from django.db import models
from django.contrib.auth.models import User
from App.models import *

# Create your models here.
class hosp_details(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    hosp_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=100, null = False, blank=False)
    hosp_wallet = models.IntegerField(blank=True, null=True)
    def __str__(self):
        if self.hosp_name==None:
            return "ERROR NAME IS NULL"
        return self.hosp_name
    
    @property
    def get_wallet_total(self):
        hosptot = self.billing_set.all()
        total=0
        for item in hosptot:
            if item.cli is None and item.trans_id is not None:
                total += item.get_fund
            else:
                total = 0
            self.hosp_wallet = total
        return self.hosp_wallet


class hospital(models.Model):
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=50)
    category_name = models.CharField(max_length=100)
    surgery = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    district_name = models.CharField(max_length=200)
    preauth_date = models.CharField(max_length=100)
    preauth_amt = models.IntegerField(null=True)
    claim_date = models.CharField(max_length=100)
    claim_amount = models.IntegerField()
    hosp_name = models.CharField(max_length=50)
    hosp_type = models.CharField(max_length=50)
    hosp_location = models.CharField(max_length=200)
    hosp_district = models.CharField(max_length=200)
    surgery_date = models.CharField(max_length=100)

    def __str__(self):
        if self.id==None:
            return "ERROR NAME IS NULL"
        return self.id

'%Y-%m-%d' #'2010-11-20'
'%m/%d/%Y' #'10/15/2021'
'%m/%d/%y' #'08/21/21'


class HospNotification(models.Model):
    notf = models.CharField(max_length=100,blank=True,null=True)
    hosp = models.ForeignKey(hosp_details, on_delete=models.SET_NULL, null=True)
    bks = models.ForeignKey("Insurance.Bank", on_delete=models.SET_NULL, null=True)


