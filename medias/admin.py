from django.contrib import admin
from .models import Music, Video, Photo
from adminpage.baseAdmin import BaseAdmin


@admin.register(Photo)
class PhotoAdmin(BaseAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    readonly_fields = [
        "img_preview"
    ]

@admin.register(Video)
class VideoAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )


@admin.register(Music)
class MusicAdmin(BaseAdmin):
    list_display = (
        "__str__",
    )