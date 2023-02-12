from django.contrib import admin
from .models import Bank
from adminpage.baseAdmin import BaseAdmin

@admin.register(Bank)
class BankAdmin(BaseAdmin):
    list_display = (
        "bankname",
        "bankcode",
    )