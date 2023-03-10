from django.contrib import admin
from adminpage.baseAdmin import BaseAdmin
from .models import Genre, Artist


@admin.register(Genre)
class GenreAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )


@admin.register(Artist)
class ArtistAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )