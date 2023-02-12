from django.contrib import admin
from adminpage.baseAdmin import BaseAdmin

class GenreAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )