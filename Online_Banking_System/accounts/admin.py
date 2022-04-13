from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(BankAccount)
admin.site.register(Transections)
admin.site.register(Benificiary)