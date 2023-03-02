from django.contrib import admin
from .models import Banner
from adminpage.baseAdmin import BaseAdmin

@admin.register(Banner)
class BankAdmin(BaseAdmin):
    list_display = (
        "title",
        "context",
        "image",
        "external_link",
    )

    