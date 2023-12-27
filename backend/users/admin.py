from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Shown in Django Admin List
    list_display = UserAdmin.list_display + \
        ('id','is_banned','is_superuser','is_teacher','is_student')
    # Editable fields per instance
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_banned','is_teacher','is_student')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
