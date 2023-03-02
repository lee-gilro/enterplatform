from django.contrib import admin
from adminpage.baseAdmin import BaseAdmin
from .models import Notice, Faq


@admin.register(Notice)
class NoticeAdmin(BaseAdmin):
    list_display = (
        "__str__",
    
    )


@admin.register(Faq)
class FaqAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )