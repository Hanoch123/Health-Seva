from typing import ContextManager
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
import hashlib
import json
from datetime import datetime
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from App.forms import *
from .forms import *
from App.filters import *
from .models import *

from multi_form_view import MultiModelFormView

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureHome(request):
     context ={}
     return render(request, 'insurance_home.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureProfile(request):
     context ={}
     return render(request, 'ins_profile.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def PlanDetails(request, ins_no):
     bks = BankInsurance.objects.get(id = ins_no)
     context ={'bks':bks}
     return render(request, 'plan_dets.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsurePlans(request):
     banks = BankInsurance.objects.all()
     context ={'banks':banks}
     return render(request, 'plans.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureClients(request):
     bks = Bank.objects.get(user = request.user)
     banks = bks.bankinsurance_set.all()
     details = bks.userdetails_set.all()
     print(details)
     statfil = StatusFilter(request.GET, queryset=details)
     details = statfil.qs
     print(details)
     context ={'details':details,'bks':bks,'banks':banks,'statfil':statfil}
     return render(request, 'clients.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureClaims(request):
     bks = Bank.objects.get(user = request.user)
     details = bks.billing_set.all()
     # print(details)
     statfil = ClaStatusFilter(request.GET, queryset=details)
     details = statfil.qs
     # print(details)
     context ={'details':details,'statfil':statfil}
     return render(request, 'claimings.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureReimburese(request):
     bks = Bank.objects.get(user = request.user)
     details = bks.billing_set.all()
     # print(details)
     statfil = ClaStatusFilter(request.GET, queryset=details)
     details = statfil.qs
     # print(details)
     context ={'details':details,'statfil':statfil}
     return render(request, 'reimburesement.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureCliDetails(request, cl_no):
     details = UserDetails.objects.get(id=cl_no)
     if request.method == "POST":
          form = UpdateStatus(request.POST, instance=details,prefix='form')
          form2 = Notify(request.POST, prefix='form2')
          if form.is_valid() and form2.is_valid():
               ok = form.save(commit=False)
               task = form2.save(commit=False)
               my_cli = Client.objects.get(user = details.cli.user)
               my_bk = Bank.objects.get(user = request.user)
               task.cli = my_cli
               task.bks = my_bk
               if details.status == 'Approved':
                    pol = GeneratePolicyNo(details.banks.bankname)
                    stri = 'Congartulations your application is approved! Your policy number is '+ pol
                    task.inc_notf = stri
                    ok.policy_no = pol
               elif details.status == 'Denied':
                    stri = 'Sorry but your application was denied due to ' + task.inc_notf
                    task.inc_notf = stri
               task.save()
               ok.save()        
               messages.success(request, " " + details.cli.firstname + "'s Application is " + details.status)
               return redirect('insclients')
     else:
          form = UpdateStatus(prefix='form')
          form2 = Notify(prefix='form2')
     context ={'details':details,'form':form,'form2':form2}
     return render(request, 'cli_details.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureClaimDetails(request, dets_no):
     details = Billing.objects.get(id=dets_no)
     clie = Client.objects.filter(user = details.cli.user)
     now = datetime.now()
     dt_date = now.strftime("%d/%m/%Y")
     dt_time = now.strftime("%H:%M:%S")
     if request.method == "POST":
          form = UpdateClaimStatus(request.POST, instance=details,prefix='form')
          form2 = Notify(request.POST, prefix='form2')
          if form.is_valid() and form2.is_valid():
               ok = form.save(commit=False)
               task = form2.save(commit=False)
               my_cli = Client.objects.get(user = details.cli.user)
               my_bk = Bank.objects.get(user = request.user)
               task.cli = my_cli
               task.bks = my_bk
               if details.status == 'Approved':
                    trans = GenerateTransID(details.banks.bankname)
                    stri = task.inc_notf + 'Congartulations your claim is approved! Your Transaction ID is '+ trans
                    task.inc_notf = stri
                    ok.trans_id = trans
                    ok.cl_date = dt_date
                    ok.cl_time = dt_time
               elif details.status == 'Denied':
                    stri = 'Sorry but your claim was denied due to ' + task.inc_notf
                    task.inc_notf = stri
                    ok.cl_date = dt_date
                    ok.cl_time = dt_time
               task.save()
               ok.save()        
               messages.success(request, " " + details.cli.firstname + "'s Application is " + details.status)
               return redirect('inshome')
     else:
          form = UpdateClaimStatus(prefix='form')
          # form1 = UpdateWallet(prefix='form1')
          form2 = Notify(prefix='form2')
     context ={'details':details,'form':form,'form2':form2}
     return render(request, 'claiming_dets.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def InsureReimbureseDetails(request, dets_no):
     details = Billing.objects.get(id=dets_no)
     now = datetime.now()
     dt_date = now.strftime("%d/%m/%Y")
     dt_time = now.strftime("%H:%M:%S")
     if request.method == "POST":
          form = UpdateClaimStatus(request.POST, instance=details,prefix='form')
          form2 = HospNotify(request.POST, prefix='form2')
          if form.is_valid() and form2.is_valid():
               ok = form.save(commit=False)
               task = form2.save(commit=False)
               my_cli = hosp_details.objects.get(user = details.hosp.user)
               my_bk = Bank.objects.get(user = request.user)
               task.hosp = my_cli
               task.bks = my_bk
               if details.status == 'Approved':
                    trans = GenerateTransID(details.banks.bankname)
                    stri = task.notf + 'Congartulations your claim is approved! Your Transaction ID is '+ trans
                    task.notf = stri
                    ok.trans_id = trans
                    ok.cl_date = dt_date
                    ok.cl_time = dt_time
               elif details.status == 'Denied':
                    stri = 'Sorry but your claim was denied due to ' + task.notf
                    task.notf = stri
                    ok.cl_date = dt_date
                    ok.cl_time = dt_time
               task.save()
               ok.save()        
               messages.success(request, " " + details.hosp.hosp_name + "'s Application is " + details.status)
               return redirect('inshome')
     else:
          form = UpdateClaimStatus(prefix='form')
          # form1 = UpdateWallet(prefix='form1')
          form2 = HospNotify(prefix='form2')
     context ={'details':details,'form':form,'form2':form2}
     return render(request, 'reimburese_dets.html', context)

@login_required(login_url='inslogin')
@allowed_users(allowed_roles=['Admin', 'Insurance'])
def AddPlan(request):
     form = NewPlan()
     if request.method == 'POST':
          form = NewPlan(request.POST,request.FILES)
          if form.is_valid():
               task = form.save(commit=False)
               my_bk = Bank.objects.get(user = request.user)
               task.Bk = my_bk
               task.save()
               messages.success(request, 'Plan Successfully added ')
               return redirect('inshome')

     context = {'form': form}
     return render(request, 'new_plan.html', context)

def GeneratePolicyNo(str1):
     str2 = str1[0: 3]
     str2 = str2.upper()
     now = datetime.now()
     dt = int(now.strftime("%d%m%y%H%M%S"))
     ok1 = random.randint(0,999999999999)
     ok2 = str(dt+ok1)
     pol_no = str2+ok2
     print(pol_no)
     return pol_no

def GenerateTransID(str1):
     now = datetime.now()
     print(now)
     dt = int(now.strftime("%d%m%y%H%M%S"))
     print(dt)
     ok1 = random.randint(0,999999999999)
     ok2 = dt+ok1
     encoded_block = json.dumps(ok2,sort_keys=True).encode()
     hashed_block = hashlib.sha256(encoded_block).hexdigest()
     return hashed_block

def InsureRegister(request):
      if request.user.is_authenticated:
            return redirect('inshome')
      else:   
        form = CreateUserForm()
        if request.method == "POST":
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')


                    Bank.objects.create(
                            user = user,
                            bankname = username,
                            email = email,
                            )

                    group = Group.objects.get(name='Insurance')
                    user.groups.add(group)

                    messages.success(request, 'Account was successfully created for ' + username)


                    return redirect('inspolicy')
                
        context = {'form': form}
        return render(request, 'Reg.html', context)
      
def InsureLogin(request):
      if request.user.is_authenticated:
            return redirect('inshome')
      else:   
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username = username, password = password)

                if user is not None:
                    auth_login(request, user)
                    return redirect('inshome')
                
                else:
                    messages.info(request, 'Username or Password is Incorrect')
                    
        context = {}
        return render(request, 'Log.html', context)
      
def InsurePolicy(request):
     form = UploadForm()
     if request.method == 'POST':
          form = UploadForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, 'Plan Successfully added ')
               return redirect('inslogin')

     context = {'form': form}
     return render(request, 'policy.html', context)

def InsureLogout(request):
      logout(request)
      return redirect('index')