from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['description']
    # list_display = ['account', 'description', 'date', 'value', 'function']