from typing import ContextManager
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import JsonResponse
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
from Insurance.forms import *
from Insurance.models import *
from App.models import *
from App.forms import *
from App.filters import *
from .models import *

# Create your views here.

# def hospital_upload(request):
#     if request.method == 'POST':
#         hospital_resources = HospitalResource()
#         dataset = Dataset()
#         new_file = request.FILES['myfile']

#         if not new_file.name.endswith('csv'):
#             messages.info(request, 'wrong format')
#             return render (request, 'upload.html')
        
#         imported_data = dataset.load(new_file.read(), format='csv')
#         for data in imported_data:
#             value = hospital(
#                 data[0],
#                 data[1],
#                 data[2],
#                 data[3]
#             )
#             value.save()
#     return render(request, 'upload.html')


@login_required(login_url='hosplogin')
@allowed_users(allowed_roles=['Admin', 'Healthcare'])
def HospHome(request):
     usr = hosp_details.objects.get(user = request.user)
     coun = HospNotification.objects.filter(hosp = usr).count()
     context = {'coun':coun}
     return render(request, 'hosp_home.html', context)

@login_required(login_url='hosplogin')
@allowed_users(allowed_roles=['Admin','Healthcare'])
def HospWallet(request):
     usr = hosp_details.objects.get(user = request.user)
     notify = HospNotification.objects.all()
     coun = HospNotification.objects.filter(hosp = usr).count()
     claims = Billing.objects.all()

     context ={'notify':notify,'coun':coun,'claims':claims,'usr':usr}
     return render(request, 'hosp_wallet.html', context)

@login_required(login_url='hosplogin')
@allowed_users(allowed_roles=['Admin', 'Healthcare'])
def HospNotifs(request):
     usr = hosp_details.objects.get(user = request.user)
     hospnotify = HospNotification.objects.all()
     coun = HospNotification.objects.filter(hosp = usr).count()
     notifs = HospNotification.objects.all()
     context = {'notifs':notifs,'hospnotify':hospnotify,'coun':coun}
     return render(request, 'hosp_notifs.html', context)

@login_required(login_url='hosplogin')
@allowed_users(allowed_roles=['Admin', 'Healthcare'])
def ClaimAppr(request):
     hosp = hosp_details.objects.get(user = request.user)
     usr = hosp_details.objects.get(user = request.user)
     coun = HospNotification.objects.filter(hosp = usr).count()
     details = hosp.billing_set.all()
     # print(details)
     statfil = HospStatusFilter(request.GET, queryset=details)
     details = statfil.qs
     # print(details)
     context ={'details':details,'statfil':statfil,'coun':coun}
     return render(request, 'hosp_appr.html', context)

@login_required(login_url='hosplogin')
@allowed_users(allowed_roles=['Admin', 'Healthcare'])
def HospApproval(request, appr_no):
     usr = hosp_details.objects.get(user = request.user)
     coun = HospNotification.objects.filter(hosp = usr).count()
     details = Billing.objects.get(id=appr_no)
     if request.method == "POST":
          form = UpdateHospStatus(request.POST, instance=details,prefix='form')
          form1 = Notify(request.POST, prefix='form1')
          if form.is_valid() and form1.is_valid():
               task = form.save(commit=False)
               task1 = form1.save(commit=False)
               my_cli = Client.objects.get(user = details.cli.user)
               my_bk = Bank.objects.get(user = details.banks.user)
               task1.cli = my_cli
               task1.bks = my_bk
               if details.hosp_status == 'Denied':
                    task.status = "Denied"
                    stri = 'Sorry but your claim was denied due to'+task1.inc_notf
                    task1.inc_notf = stri
               elif details.hosp_status == 'Approved':
                    stri = 'Congartulations your claim is approved by '+ details.hosp.hosp_name
                    task1.inc_notf = stri
               task.save()
               task1.save()
               messages.success(request, details.cli.firstname + "'s Application is " + details.hosp_status)
               return redirect('hosphome')
     else:
          form = UpdateHospStatus(prefix='form')
          form1 = Notify(prefix='form1')
     context ={'details':details,'form':form,'form1':form1,'coun':coun}
     return render(request, 'hosp_claims.html', context)

@login_required(login_url='hosplogin')
@allowed_users(allowed_roles=['Admin','Healthcare'])
def HospClaims(request):
     usr = hosp_details.objects.get(user = request.user)
     coun = HospNotification.objects.filter(hosp = usr).count()
     claims = Billing.objects.all()

     context ={'claims':claims,'coun':coun}
     return render(request, 'hosp_claimings.html', context)

@login_required(login_url='hosplogin')
@allowed_users(allowed_roles=['Admin','Healthcare'])
def HospNewClaim(request):
     usr = hosp_details.objects.get(user = request.user)
     coun = HospNotification.objects.filter(hosp = usr).count()
     now = datetime.now()
     dt_date = now.strftime("%d/%m/%Y")
     dt_time = now.strftime("%H:%M:%S")
     # notify = Notification.objects.all()
     # coun = Notification.objects.filter(cli = usr).count()
     form = HospClaiming()
     if request.method == 'POST':
          form = HospClaiming(request.POST,request.FILES)
          if form.is_valid():
               task = form.save(commit=False)
               my_cli = hosp_details.objects.get(user=request.user)
               task.hosp = my_cli
               task.hosp_name = my_cli.hosp_name
               task.ap_date = dt_date
               task.ap_time = dt_time
               task.status = "Pending"
               task.hosp_status = "Approved"
               task.save()
               messages.success(request, 'Your claim is successfully submitted!')
               return redirect('hosphome')

     context ={'form':form,'coun':coun}
     return render(request, 'hosp_newclaim.html', context)

def HospRegister(request):
      if request.user.is_authenticated:
            return redirect('hosphome')
      else:   
        form = CreateUserForm()
        if request.method == "POST":
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')
                    wal = 0


                    hosp_details.objects.create(
                            user = user,
                            hosp_name = username,
                            email = email,
                            hosp_wallet = wal,
                            )

                    group = Group.objects.get(name='Healthcare')
                    user.groups.add(group)

                    messages.success(request, 'Account was successfully created for ' + username)


                    return redirect('hosplogin')
                
        context = {'form': form}
        return render(request, 'hosp_register.html', context)
      
def HospLogin(request):
      if request.user.is_authenticated:
            return redirect('hosphome')
      else:   
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username = username, password = password)

                if user is not None:
                    auth_login(request, user)
                    return redirect('hosphome')
                
                else:
                    messages.info(request, 'Username or Password is Incorrect')
                    
        context = {}
        return render(request, 'hosp_login.html', context)

def HospLogout(request):
      logout(request)
      return redirect('index')
