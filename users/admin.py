from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.safestring import mark_safe

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
            "fields":("avatar","imgThumbnail","username","password","first_name","last_name","email","is_artist","gender","language","currency",),
            "classes" : ("wide",),
            },
        ),
        ("Permissions", 
            {
            "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            "classes": ("collapse",),
            }
        ),
        (
            "Important Dates", 
            {
            "fields": ("last_login","date_joined"),
            "classes" : ("collapse",),
            },

            ),
       
    
    )
    readonly_fields = ('avatar','imgThumbnail')
    @admin.display(
  		description="이미지 미리보기"
	)
    def imgThumbnail(self,obj):
        return mark_safe(f"<img src='{obj.user_img_url}' />")