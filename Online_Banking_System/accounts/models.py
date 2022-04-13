from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
upload_to='profile_images'
from datetime import datetime
from django.conf import settings
import os

media_root = settings.MEDIA_ROOT
path = os.path.join(media_root, 'default.jpg')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Image = models.ImageField(default=path, upload_to='profile_images')
    mobile = models.BigIntegerField(null=False)
    dob = models.DateField(null=False)
        
    gender = models.CharField(max_length=10)
    address = models.TextField(default="Address not given")
    city = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.user.username
 
class BankAccount(models.Model):
    user = models.ForeignKey(
        User,
        related_name='account',
        on_delete=models.CASCADE,
    )
    
    ACCOUNT_TYPE_CHOICE = (
        ("CURRENT", "Current"),
        ("SAVING", "Saving"),
        ("SALARY", "Salary"),
        ("FIXED_DEPOSITE", "Fixed Deposite"),
        ("RECURRING_DEPOSITE", "Recurring Deposite"),
    )
    
    account_type = models.CharField(choices=ACCOUNT_TYPE_CHOICE,max_length=20)
    
    account_no = models.BigIntegerField(unique=True)
    IFSC_Code = models.CharField(unique=True, max_length=10)
    
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    
    Minimum_Balance = models.DecimalField(default=3000, decimal_places=2, max_digits=6)
    created_on = models.DateTimeField()
    
class Transections(models.Model):
    user = models.ForeignKey(
        User,
        related_name='transections',
        on_delete=models.CASCADE,
    ) 
    
    account_no = models.BigIntegerField()

    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    STATUS = (
        ("CREDITE", "Credit"),
        ("DEBIT", "Dabit"),
    )
    
    status = models.CharField(choices=STATUS,max_length=10)
    
    show_to_user = models.BooleanField(default=True)
    

class Benificiary(models.Model):
    
    user = models.ForeignKey(
        User,
        related_name='benificiary',
        on_delete=models.CASCADE,
    )
    
    recievers_account_no = models.BigIntegerField()
    
    IFSC_Code = models.CharField(max_length=10)
    
    max_limit = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    
    STATUS = (
        ("ACTIVE", "Active"),
        ("PENDING", "Pending"),
    )
    
    status = models.CharField(choices=STATUS,max_length=10, default="Pending")
    
    timestamp = models.DateTimeField(auto_now_add=True) 