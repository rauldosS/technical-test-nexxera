from django.contrib import admin
from .models import Bank, Account

# Register your models here.
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['bank', 'number', 'name', 'validity', 'balance', 'cvv', 'active']