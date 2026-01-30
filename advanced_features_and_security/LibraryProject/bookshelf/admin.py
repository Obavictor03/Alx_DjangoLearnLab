from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
admin.site.register(Book)

class Bookadmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publication_year')
    list_filter = ('title', 'publication_year')
    search_fields = ('title', 'author')
    ordering = ('title')
    list_per_page = 20


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