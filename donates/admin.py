from django.contrib import admin
from adminpage.baseAdmin import BaseAdmin
from .models import Donate


@admin.register(Donate)
class DonateAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )
