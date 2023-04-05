from typing import ContextManager
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from datetime import datetime
import hashlib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import Group
from .decorators import *
from .forms import *
from Insurance.models import *
from Insurance.forms import *
from hospital.models import *
from .models import *
from .filters import *
# Create your views here.

# @login_required(login_url='login')
def Index(request):
      context = {}
      return render(request, 'index.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def Home(request):
      usr = Client.objects.get(user = request.user)
      notify = Notification.objects.all()
      coun = Notification.objects.filter(cli = usr).count()
      context = {'notify':notify,'coun':coun}
      return render(request, 'home.html', context)

def MainPage(request):
      usr = Client.objects.get(user = request.user)
      notify = Notification.objects.all()
      coun = Notification.objects.filter(cli = usr).count()
      context = {'notify':notify,'coun':coun}
      return render(request, 'main.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def CliNotify(request, not_no):
      usr = Client.objects.get(user = request.user)
      notify = Notification.objects.all()
      coun = Notification.objects.filter(cli = usr).count()
      notifs = Notification.objects.get(id=not_no)
      if request.method == 'POST':
           Notification.objects.get(id=not_no).delete()
           print('deleted')
           return redirect('home')
      else:
           print('hi')
      context = {'notifs':notifs,'notify':notify,'coun':coun}
      return render(request, 'notifications.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def InsDetails(request, bk_no):
      user = request.user.username
      now = datetime.now()
      dt_date = now.strftime("%d/%m/%Y")
      dt_time = now.strftime("%H:%M:%S")
      bks = BankInsurance.objects.get(id=bk_no)
      clients = Client.objects.get(user = request.user)
      notify = Notification.objects.all()
      coun = Notification.objects.filter(cli = clients).count()
      form = UploadDocs()
      if request.method == 'POST':
           form = UploadDocs(request.POST, request.FILES)
           if form.is_valid():
                task = form.save(commit=False)
                my_p = Client.objects.get(user=request.user)
                my_b = Bank.objects.get(user = bks.Bk.user)
                task.cli = my_p
                task.banks = my_b
                task.bank_ins = bks
                task.date = dt_date
                task.time = dt_time
                task.status = "Pending"
                task.save()
                messages.success(request, 'Hey '+ user +', The Policy is Applied Successfully! Yow will be Notified as soon as the Processing is completed! ')
                return redirect('home')
      # banks = bks.bankinsurance_set.all()
      context = {'bks':bks,'form':form,'clients':clients,'notify':notify,'coun':coun}
      return render(request, 'ins_details.html', context)


def register(request):
      if request.user.is_authenticated:
            return redirect('home')
      else:   
        form = CreateUserForm()
        if request.method == "POST":
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')
                    firstname = request.POST.get('firstname')
                    lastname = request.POST.get('lastname')
                    ph_num = request.POST.get('phone')                                                                               
                    dob = request.POST.get('dob')
                    Address = request.POST.get('address')
                    State = request.POST.get('state')
                    City = request.POST.get('city')
                    Occupation = request.POST.get('occ')
                    NetWorth = request.POST.get('networth')
                    wal = 0


                    Client.objects.create(
                            user = user,
                            username = username,
                            email = email,
                            firstname = firstname,
                            lastname = lastname,
                            ph_num = ph_num,
                            dob = dob,
                            Address = Address,
                            State = State,
                            City = City,
                            Occupation = Occupation,
                            NetWorth = NetWorth,
                            wallet = wal,
                            )
                    
                    dic = {'username':username,
                           'email': email,
                           'firstname': firstname,
                           'lastname': lastname,
                           'ph_num': ph_num,
                           'dob' : dob,
                           'Address' : Address,
                           'State': State,
                           'City': City,
                           'Occupation': Occupation,
                           'NetWorth': NetWorth,
                           }

                    encoded_block = json.dumps(dic,sort_keys=True).encode()
                    hashed_block = hashlib.sha256(encoded_block).hexdigest()

                    Hashed_Client.objects.create(
                        cli_user = user,
                        hashed_details = hashed_block,
                    )      

                    group = Group.objects.get(name='Client')
                    user.groups.add(group)

                    messages.success(request, 'Account was successfully created for ' + hashed_block)


                    return redirect('login')
                
        context = {'form': form}
        return render(request, 'register.html', context)

def login(request):
      if request.user.is_authenticated:
            return redirect('home')
      else:   
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username = username, password = password)

                if user is not None:
                    auth_login(request, user)
                    return redirect('home')
                
                else:
                    messages.info(request, 'Username or Password is Incorrect')
                    
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
      logout(request)
      return redirect('index')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def Insurance(request):
     usr = Client.objects.get(user = request.user)
     notify = Notification.objects.all()
     coun = Notification.objects.filter(cli = usr).count()
     banks = BankInsurance.objects.all()

     bkfilter = BankFilter(request.GET, queryset=banks)
     banks = bkfilter.qs

     context ={'banks':banks, 'bkfilter':bkfilter,'notify':notify,'coun':coun}
     return render(request, 'insurance.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def MyPlans(request):
     usr = Client.objects.get(user = request.user)
     notify = Notification.objects.all()
     coun = Notification.objects.filter(cli = usr).count()
     dets = UserDetails.objects.all()

     #bkfilter = BankFilter(request.GET, queryset=banks)
     #banks = bkfilter.qs

     context ={'notify':notify,'coun':coun,'dets':dets}
     return render(request, 'myplans.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def NewClaim(request):
     usr = Client.objects.get(user = request.user)
     now = datetime.now()
     dt_date = now.strftime("%d/%m/%Y")
     dt_time = now.strftime("%H:%M:%S")
     notify = Notification.objects.all()
     coun = Notification.objects.filter(cli = usr).count()
     form = Claiming()
     if request.method == 'POST':
          form = Claiming(request.POST,request.FILES)
          if form.is_valid():
               task = form.save(commit=False)
               my_cli = Client.objects.get(user=request.user)
               task.cli = my_cli
               task.ap_date = dt_date
               task.ap_time = dt_time
               task.status = "Pending"
               task.hosp_status = "Pending"
               task.save()
               messages.success(request, 'Your claim is successfully submitted!')
               return redirect('home')
#      dets = UserDetails.objects.all()

     #bkfilter = BankFilter(request.GET, queryset=banks)
     #banks = bkfilter.qs

     context ={'notify':notify,'coun':coun,'form':form}
     return render(request, 'new_claim.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def Claims(request):
     usr = Client.objects.get(user = request.user)
     notify = Notification.objects.all()
     coun = Notification.objects.filter(cli = usr).count()
     claims = Billing.objects.all()

     context ={'notify':notify,'coun':coun,'claims':claims}
     return render(request, 'claims.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def CliWallet(request):
     usr = Client.objects.get(user = request.user)
     notify = Notification.objects.all()
     coun = Notification.objects.filter(cli = usr).count()
     claims = Billing.objects.all()

     context ={'notify':notify,'coun':coun,'claims':claims,'usr':usr}
     return render(request, 'wallet.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Client'])
def ClaimDetails(request, bil_no):
     usr = Client.objects.get(user = request.user)
     notify = Notification.objects.all()
     coun = Notification.objects.filter(cli = usr).count()
     claim = Billing.objects.get(id = bil_no)

     context ={'notify':notify,'coun':coun,'claim':claim}
     return render(request, 'claim_details.html', context)
