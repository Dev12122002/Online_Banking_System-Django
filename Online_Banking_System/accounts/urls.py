from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('completeProfile', views.completeProfile, name='completeProfile'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('removePic', views.removePic, name='removePic'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('cancelUpdateProfile', views.cancelUpdateProfile, name='cancelUpdateProfile'),
    path('createBankAccount', views.createBankAccount, name='createBankAccount'),
    path('deleteBankAccount/<int:id>', views.deleteBankAccount, name='deleteBankAccount'),
    path('deleteBankAccountByAdmin/<int:id>', views.deleteBankAccountByAdmin, name='deleteBankAccountByAdmin'),
    # path('myAccount', views.myAccount, name='myAccount'),
    # path('fundTransfer', views.fundTransfer, name='fundTransfer'),
    path('transfer', views.transfer, name='transfer'),
    # path('myTransections', views.myTransections, name='myTransections'),
    path('clearTransections', views.clearTransections, name='clearTransections'),
    path('deleteUserAccount', views.deleteUserAccount, name='deleteUserAccount'),
    path('deleteUserAccountByAdmin/<int:id>', views.deleteUserAccountByAdmin, name='deleteUserAccountByAdmin'),
    # path('manageBenificiary', views.manageBenificiary, name='manageBenificiary'),
    path('AddBenificiary', views.AddBenificiary, name='AddBenificiary'),
    path('deleteBenificiary/<int:id>', views.deleteBenificiary, name='deleteBenificiary'),
    # path('payToBenificiary', views.payToBenificiary, name='payToBenificiary'),
    path('payBenificiary', views.payBenificiary, name='payBenificiary'),
    # path('adminHome', views.adminHome, name='adminHome'),
    # path('allAccounts', views.allAccounts, name='allAccounts'),
    # path('allBenificiaries', views.allBenificiaries, name='allBenificiaries'),
    # path('allTransections', views.allTransections, name='allTransections'),
    # path('accountTransections', views.accountTransections, name='accountTransections'),
    # path('userTransections', views.userTransections, name='userTransections'),
    # path('allUsers', views.allUsers, name='allUsers'),
    path('activateBenificiary/<int:id>', views.activateBenificiary, name='activateBenificiary'),
    path('deactivateBenificiary/<int:id>', views.deactivateBenificiary, name='deactivateBenificiary'),
    # path('userBenificiaries', views.userBenificiaries, name='userBenificiaries'),

    # path('forgot-password', views.forgotpassword, name='forgot-password'),
    # path('reset-password', views.reset_password, name='forgot-password'),
    # path('error', views.error, name='error')
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    #  auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
    auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]