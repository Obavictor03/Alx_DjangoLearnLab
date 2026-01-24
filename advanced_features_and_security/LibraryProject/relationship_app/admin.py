from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
        "date_of_birth",
        "profile_photo",
    )

    list_filter = (
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
    )

    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("email", "date_of_birth", "profile_photo")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
         ),
         ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None, {
                "classes": ("Wide",), "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "date_of_birth",
                    "profile_picture",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )