from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class UploadForm(ModelForm):
    Bk = forms.TextInput()
    no_plans = forms.TextInput()
    features = forms. TextInput()
    desc = forms.TextInput()
    exclusions = forms.TextInput()
    coverage = forms.TextInput()
    plan_type = forms.TextInput()
    insurance_for = forms.TextInput()
    tenure = forms.TextInput()
    hospitals = forms.TextInput()
    premium = forms.TextInput()
    Brochure = forms.FileInput()
    class Meta:
        model = BankInsurance
        fields = ['Bk','no_plans', 'features', 'desc', 'exclusions', 'coverage', 'plan_type', 'insurance_for', 'tenure', 'hospitals', 'premium', 'Brochure']


class Claiming(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['banks','policy_no','bill','doc_name','hosp','admit_date','disc_date','ap_date','ap_time']
        widgets = {
            'admit_date': forms.DateInput(attrs={'type':'date','class':'form-date'}),
            'disc_date': forms.DateInput(attrs={'type':'date','class':'form-date'}),
        }

class HospClaiming(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['banks','policy_no','bill','doc_name','admit_date','disc_date','ap_date','ap_time']
        widgets = {
            'admit_date': forms.DateInput(attrs={'type':'date','class':'form-date'}),
            'disc_date': forms.DateInput(attrs={'type':'date','class':'form-date'}),
        }