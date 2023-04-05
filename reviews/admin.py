from django.contrib import admin
from .models import Review
from adminpage.baseAdmin import BaseAdmin

# Register your models here.
@admin.register(Review)
class ReviewAdmin(BaseAdmin):

    list_display = (
        "__str__",
    )

    list_filter = (
        "user__is_artist",

    )