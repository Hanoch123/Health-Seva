from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from App.models import *
from Insurance.models import *
from hospital.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']


class ClientDets(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['user']



class UploadDocs(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['proof','inc_proof','pic']

class UpdateStatus(forms.ModelForm):
    policy_no = forms.CharField(required=False)
    class Meta:
        model = UserDetails
        fields = ['status','policy_no']
        widgets = {
            'status': forms.Select(attrs={'class':'okay'}),
        }

class UpdateClaimStatus(forms.ModelForm):
    cl_date = forms.CharField(required=False)
    cl_time = forms.CharField(required=False)
    class Meta:
        model = Billing
        fields = ['status','rel_fund','cl_date','cl_time']
        widgets = {
            'status': forms.Select(attrs={'class':'okay'}),
        }

class UpdateHospStatus(forms.ModelForm):
    status = forms.ChoiceField(required=False)
    class Meta:
        model = Billing
        fields = ['hosp_status','status']
        widgets = {
            'hosp_status': forms.Select(attrs={'class':'okay'}),
        }

class UpdateWallet(forms.ModelForm):
    wallet = forms.IntegerField(required=False)
    class Meta:
        model = Client
        fields = ['wallet']


class Notify(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['inc_notf']
        widgets = {
            'inc_notf': forms.Textarea(attrs={'class':'zee'}),
        }

class HospNotify(forms.ModelForm):
    class Meta:
        model = HospNotification
        fields = ['notf']
        widgets = {
            'notf': forms.Textarea(attrs={'class':'zee'}),
        }