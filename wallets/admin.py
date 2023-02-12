from django.contrib import admin
from .models import Wallet
from adminpage.baseAdmin import BaseAdmin


@admin.register(Wallet)
class WalletAdmin(BaseAdmin):
    list_display = (
        "owner",
        "bisou",
        "bank",
        "account",
    )

    list_filter = (
        "bisou",
    )

    search_fields = (
        "onwer",
    )