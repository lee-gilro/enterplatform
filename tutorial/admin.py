from django.contrib import admin
from adminpage.baseAdmin import BaseAdmin
from .models import Tutorial, Curation


@admin.register(Tutorial)
class TutorialAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )


@admin.register(Curation)
class CurationAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )