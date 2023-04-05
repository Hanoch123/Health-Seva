from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null = False, blank=False)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    ph_num = models.CharField(max_length=10, null=False, blank=False)
    dob = models.DateField()
    Address = models.CharField(max_length=50, null=False, blank=False)
    State = models.CharField(max_length=50, null=False, blank=False)
    City = models.CharField(max_length=50, null=False, blank=False)
    Occupation = models.CharField(max_length=50, null=False, blank=False)
    NetWorth = models.CharField(max_length=50, null=False, blank=False)
    wallet = models.IntegerField(blank=True, null=True)

    
    def __str__(self):
        if self.username==None:
            return "ERROR NAME IS NULL"
        return self.username
    
    @property
    def get_total(self):
        clietot = self.billing_set.all()
        total = sum([item.get_fund for item in clietot])
        self.wallet = total
        return self.wallet



class Hashed_Client(models.Model):
    cli_user = models.OneToOneField(User, on_delete=models.CASCADE)
    hashed_details = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.hashed_details

class Notification(models.Model):
    inc_notf = models.CharField(max_length=100,blank=True,null=True)
    cli = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    bks = models.ForeignKey("Insurance.Bank", on_delete=models.SET_NULL, null=True)

# class WalletMon(models.Model):
#     cli = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
#     tot_amount = models.BigIntegerField(blank=True, null=True)
    
#     def __str__(self):
#         if self.cli.firstname==None:
#             return "ERROR NAME IS NULL"
#         return self.cli.firstname

# COVERAGE = (
#     ("1", "₹3 Lac"),
#     ("2", "₹5 Lac"),
#     ("3", "₹10 Lac"),
# )
# PLAN = (
#     ("1", "Base"),
#     ("2", "1 Cr Cover"),
# )
#

    # Licence = models.FileField(upload_to="licence/", max_length=250, null=True, default=None)
    # Aadhaar = models.FileField(upload_to="aadhaar/", max_length=250, null=True, default=None)
# INSURANCE = (
#     ("1", "Family"),
#     ("2", "Senior Citizen"),
#     ("3", "Individual"),
#     ("4", "Personal Accident"),
#     ("5", "Parent"),
#     ("6", "Maternity"),
#     ("7", "Child Health"),
#     ("8", "Newborn Baby"),
#     ("9", "Self-Employed"),
#     ("10", "Woman Healthcare"),
#     ("11", "Group"),
# )

# TENURE = (
#     ("1", "1 Year"),
#     ("2", "2 Years"),
#     ("3", "3 Years"),
# )

# class Insurance(models.Model):
#     bank_name = models.CharField(max_length=30, null=False, blank=False)
#     features = models.CharField(max_length=500, null=False, blank=False)
#     exclusions = models.CharField(max_length=500, null=False, blank=False)
#     coverage = models.CharField(max_length=30,choices=COVERAGE,default=1)
#     plan_type = models.CharField(max_length=30,choices=PLAN,default=1)
#     insurance_for = models.CharField(max_length=30,choices=INSURANCE,default=1)
#     tenure = models.CharField(max_length=30,choices=TENURE,default=1)
#     hospitals = models.CharField(max_length=500, null=False, blank=False)
#     premium = models.IntegerField(null=False, blank=False)
#     Brochure = models.FileField(upload_to="brochure/", max_length=250, null=True, default=None)


#     def __str__(self):
#         if self.bank_name==None:
#             return "ERROR NAME IS NULL"
#         return self.bank_name
    
# class HealthCare(models.Model):
#     hospital_name = models.CharField(max_length=30, null=False, blank=False)
#     Address = models.CharField(max_length=300, null=False, blank=False)
#     State = models.CharField(max_length=50, null=False, blank=False)
#     City = models.CharField(max_length=50, null=False, blank=False)

#     def __str__(self):
#         if self.hospital_name==None:
#             return "ERROR NAME IS NULL"
#         return self.hospital_name

