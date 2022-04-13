from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    path('myAccount', views.myAccount, name='myAccount'),
    path('fundTransfer', views.fundTransfer, name='fundTransfer'),
    path('myTransections', views.myTransections, name='myTransections'),
    path('manageBenificiary', views.manageBenificiary, name='manageBenificiary'),
    path('payToBenificiary', views.payToBenificiary, name='payToBenificiary'),
    path('adminHome', views.adminHome, name='adminHome'),
    path('allAccounts', views.allAccounts, name='allAccounts'),
    path('allBenificiaries', views.allBenificiaries, name='allBenificiaries'),
    path('allTransections', views.allTransections, name='allTransections'),
    path('accountTransections', views.accountTransections, name='accountTransections'),
    path('userTransections', views.userTransections, name='userTransections'),
    path('allUsers', views.allUsers, name='allUsers'),
    path('userBenificiaries', views.userBenificiaries, name='userBenificiaries'),
    path('userAccounts', views.userAccounts, name='userAccounts'),
    
]