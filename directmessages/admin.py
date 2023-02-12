from django.contrib import admin
from .models import ChattingRoom, Message
from adminpage.baseAdmin import BaseAdmin

@admin.register(ChattingRoom)
class ChattingRoomAdmin(BaseAdmin):
    list_display = (
        "__str__",
        "created_at",
    )

    list_filter = (
        "created_at",
    )
    

@admin.register(Message)
class MessageAdmin(BaseAdmin):
    list_display = (
        "text",
        "user",
        "room",
        "created_at",
    )

    list_filter = (
        "created_at",
    )