from django.contrib import admin
from .models import Vote, Choice
from adminpage.baseAdmin import BaseAdmin


@admin.register(Vote)
class VoteAdmin(BaseAdmin):
    list_display = (
        "owner",
        "question_text",

    )

    list_filter = (
        "owner",
    )

    fieldsets = (
        (
            "Question",
            {
                "fields":("question_text","owner",),
                "classes" : ("wide",),
            },
        ),
    )

@admin.register(Choice)
class ChoiceAdmin(BaseAdmin):
    list_display = (
        "question",
        "choice_text",
    )