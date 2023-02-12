from django.contrib import admin
from .models import Feed, WorkLog
from medias.models import Photo, Video, Music
from adminpage.baseAdmin import BaseAdmin
# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0
class VideoInline(admin.TabularInline):
    model = Video
    extra = 0
class MusicInline(admin.TabularInline):
    model = Music
    extra = 0
class WorkLogInline(admin.TabularInline):
    model = WorkLog
    extra = 0

@admin.register(Feed)
class FeedAdmin(BaseAdmin):

    list_display = (
        "user",
        "payloads",
        "backgroundimage",
        "on_public",
        "feed_name",
    )

    list_filter = (
        "on_public",
    )

    search_fields = (
        "user",
        "feed_name",
    )

    inlines = [WorkLogInline,MusicInline]
@admin.register(WorkLog)
class WorkLogAdmin(BaseAdmin):

    list_display = (
        "posted_feed",
        "payload",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    inlines = [PhotoInline, VideoInline]