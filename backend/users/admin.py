from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class UsersAdmin(UserAdmin):
    list_display = ("username", "company", "role")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Company information",
            {
                "fields": ("company", "role"),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Company information",
            {
                "fields": ("company", "role"),
            },
        ),
    )


admin.site.register(User, UsersAdmin)