from django.db import models
from django.contrib.auth.models import User
# import App.models.Client
from App.models import *
from hospital.models import *

# Create your models here.

COVERAGE = (
    ("1", "₹2 Lac"),
    ("2", "₹3 Lac"),
    ("3", "₹5 Lac"),
    ("4", "₹10 Lac"),
    ("5", "₹25 Lac"),
)
PLAN = (
    ("1", "Base"),
    ("2", "1 Cr Cover"),
)

INSURANCE = (
    ("1", "Family"),
    ("2", "Senior Citizen"),
    ("3", "Individual"),
    ("4", "Personal Accident"),
    ("5", "Parent"),
    ("6", "Maternity"),
    ("7", "Child Health"),
    ("8", "Newborn Baby"),
    ("9", "Self-Employed"),
    ("10", "Woman Healthcare"),
    ("11", "Group"),
)

TENURE = (
    ("1", "1 Year"),
    ("2", "2 Years"),
    ("3", "3 Years"),
)

STATUS = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Denied", "Denied"),
)

class Bank(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bankname = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=100, null = False, blank=False)

    def __str__(self):
        if self.bankname==None:
            return "ERROR NAME IS NULL"
        return self.bankname

class BankInsurance(models.Model):
    Bk = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    no_plans = models.CharField(max_length=50, null=False, blank=False)
    features = models.CharField(max_length=500, null=False, blank=False)
    desc = models.CharField(max_length=5000, null=True, blank=True)
    exclusions = models.CharField(max_length=500, null=False, blank=False)
    coverage = models.CharField(max_length=30,choices=COVERAGE,default=1)
    plan_type = models.CharField(max_length=30,choices=PLAN,default=1)
    insurance_for = models.CharField(max_length=30,choices=INSURANCE,default=1)
    tenure = models.CharField(max_length=30,choices=TENURE,default=1)
    hospitals = models.CharField(max_length=500, null=False, blank=False)
    premium = models.IntegerField(null=False, blank=False)
    Brochure = models.FileField(upload_to="brochure/", max_length=250, null=True, default=None)


    def __str__(self):
        if self.no_plans==None:
            return "ERROR NAME IS NULL"
        return self.no_plans
    def getval(self):
        print(self.get_insurance_for_display())
        return self.get_insurance_for_display()
    
    def gettenure(self):
        print(self.get_tenure_display())
        return self.get_tenure_display()
    def getcoverage(self):
        print(self.get_coverage_display())
        return self.get_coverage_display()
    def getplan(self):
        print(self.get_plan_type_display())
        return self.get_plan_type_display()

class UserDetails(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    banks = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    bank_ins = models.ForeignKey(BankInsurance, on_delete=models.SET_NULL, null=True)
    pic = models.ImageField(upload_to='user/',max_length=250, null=True, default=None)
    proof = models.FileField(upload_to="proof/", max_length=250, null=True, default=None)
    inc_proof = models.FileField(upload_to="inc_proof/", max_length=250, null=True, default=None)
    date = models.CharField(max_length=30, blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30,choices=STATUS,default=1)
    policy_no = models.CharField(max_length=200, blank=True, null=True)

    def getstat(self):
        return self.get_status_display()
    
class Billing(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    banks = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    hosp = models.ForeignKey(hosp_details, on_delete=models.SET_NULL, null=True)
    policy_no = models.CharField(max_length=200, blank=True, null=True)
    bill = models.FileField(upload_to="bill/", max_length=250, null=True, default=None)
    doc_name = models.CharField(max_length=50, blank=False, null=False)
    hosp_name = models.CharField(max_length=50, blank=False, null=False)
    treatment = models.CharField(max_length=500, blank=True, null=True)
    medication = models.CharField(max_length=500, blank=True, null=True)
    hosp_status = models.CharField(max_length=30,choices=STATUS,default=1)
    status = models.CharField(max_length=30,choices=STATUS,default=1)
    rel_fund = models.IntegerField(blank=True, null=True)
    trans_id = models.CharField(max_length=100, blank=True, null=True)
    ap_date = models.CharField(max_length=30, blank=True, null=True)
    ap_time = models.CharField(max_length=30, blank=True, null=True)
    cl_date = models.CharField(max_length=30, blank=True, null=True)
    cl_time = models.CharField(max_length=30, blank=True, null=True)
    admit_date = models.DateField(null=True)
    disc_date = models.DateField(null=True)

    @property
    def get_fund(self):
        return self.rel_fund

    
# class HealthCare(models.Model):
#     hospital_name = models.CharField(max_length=30, null=False, blank=False)
#     Address = models.CharField(max_length=300, null=False, blank=False)
#     State = models.CharField(max_length=50, null=False, blank=False)
#     City = models.CharField(max_length=50, null=False, blank=False)

#     def __str__(self):
#         if self.hospital_name==None:
#             return "ERROR NAME IS NULL"
#         return self.hospital_name

