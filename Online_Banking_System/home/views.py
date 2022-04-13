# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# # from django.conf import settings
# from django.contrib.auth.models import User, auth
# from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import Profile
from accounts.models import BankAccount
from accounts.models import Transections
from accounts.models import Benificiary
from datetime import datetime
import os
from django.contrib.auth.decorators import login_required
import random
from time import gmtime, strftime
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from django.http import HttpResponse

def check_user(user):
    if not user.is_active:
       return False;
    isUser = False
    if user.is_superuser == 0:
        isUser=True
    return isUser

def check_admin(user):
    if not user.is_active:
       return False;
    isAdmin = False
    if user.is_superuser:
        isAdmin=True
    return isAdmin

# @login_required(login_url='login')
@user_passes_test(check_user, login_url='login')
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")

@login_required(login_url='login')
def about(request):
    return render(request, "about.html")

from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['msg_subject']
        message = request.POST['message']
        mymessage = f" Name : {name} \n Email : {email} \n Phonen Number : {phone_number} \n Subject : {subject} \n Message : {message}"
        recipient_list = [request.user.email, ]
        messages.success(request, 'Message Sent Successfully')
        email_from = email
        recipient_list = ['dduprojects12@gmail.com', ]
        send_mail( 'Customer Contact', mymessage, email_from, recipient_list )

        return redirect('contact')
    else:
        return render(request, "contact.html")
    
    
@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html")

# @login_required(login_url='login')
@user_passes_test(check_user, login_url='login')   
def myAccount(request):
    current_user = request.user
    user = User.objects.get(username=current_user)
    bankAccounts = BankAccount.objects.filter(user_id=user.id)
    context = {'bankAccounts': bankAccounts}
    return render(request, "myAccount.html", context)

# @login_required(login_url='login')
@user_passes_test(check_user, login_url='login')  
def fundTransfer(request):
    return render(request, "fundTransfer.html")

# @login_required(login_url='login')
@user_passes_test(check_user, login_url='login')
def myTransections(request):
    current_user = request.user
    transections = Transections.objects.filter(user_id=current_user.id,show_to_user=True)
    
    if not transections:
        messages.error(request, "No transections found")
        print("transections is null")
    context = {'transections': transections}
    return render(request, "myTransections.html", context)

# @login_required(login_url='login')
@user_passes_test(check_user, login_url='login')
def manageBenificiary(request):
    current_user = request.user
    benificiaries = Benificiary.objects.filter(user_id=current_user.id)
    context = {'benificiaries': benificiaries}
    return render(request, "benificiary.html", context)

@user_passes_test(check_user, login_url='login')
def payToBenificiary(request):
    current_user = request.user
    benificiaries = Benificiary.objects.filter(user_id=current_user.id,status="Active")
    context = {'benificiaries': benificiaries}
    return render(request, "payBenificiary.html", context)

@user_passes_test(check_admin, login_url='login')
def adminHome(request):
    bankAccounts = BankAccount.objects.all()    
    context = {'bankAccounts': bankAccounts}
    return render(request, "adminHome.html", context)

@user_passes_test(check_admin, login_url='login')
def allAccounts(request):
    bankAccounts = BankAccount.objects.all()    
    context = {'bankAccounts': bankAccounts}
    return render(request, "allAccounts.html", context)

@user_passes_test(check_admin, login_url='login')
def allBenificiaries(request):
    benificiaries = Benificiary.objects.all()    
    context = {'benificiaries': benificiaries}
    return render(request, "allBenificiaries.html", context)

@user_passes_test(check_admin, login_url='login')
def allTransections(request):
    transections = Transections.objects.all()  
    context = {'transections': transections}
    return render(request, "allTransections.html", context)

@user_passes_test(check_admin, login_url='login')
def accountTransections(request):
    if request.method == "POST":
        acc_no = request.POST['acc_no']
        transections = Transections.objects.filter(account_no=int(acc_no))
        context = {'transections': transections}
        print(acc_no)
        # return render(request, "allTransections.html", context)
        return render(request, "accountTransections.html", context) 

@user_passes_test(check_admin, login_url='login')   
def userTransections(request):
    if request.method == "POST":
        uid = request.POST['uid']
        transections = Transections.objects.filter(user_id=int(uid))
        context = {'transections': transections}
        return render(request, "userTransections.html", context)

@user_passes_test(check_admin, login_url='login')  
def userAccounts(request):    
    if request.method == "POST":
        uid = request.POST['uid']
        bankAccounts = BankAccount.objects.filter(user_id=int(uid))
        context = {'bankAccounts': bankAccounts}
        return render(request, "userAccounts.html", context)
    
@user_passes_test(check_admin, login_url='login')
def allUsers(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    users = User.objects.filter(is_superuser=False) 
    context = {'users': users}
    return render(request, "allUsers.html", context) 

@user_passes_test(check_admin, login_url='login')
def userBenificiaries(request):
    if request.method == "POST":
        uid = request.POST['uid']
        benificiaries = Benificiary.objects.filter(user_id=uid)
        context = {'benificiaries': benificiaries}
        return render(request, "userBenificiaries.html", context)
    else:
        return redirect("/")    