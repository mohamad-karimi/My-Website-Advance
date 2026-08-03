from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    '''
    This class for making custome admin panel for the user
    '''
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser")
    readonly_fields = ("create_date", "update_date")
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Groups and Permissions", {"fields": ("groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        ("Authentication", {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
        ("Permissions", {
            "classes": ("wide",),
            "fields": ("is_staff", "is_active", "is_superuser"),
        }),
        ("Groups and Permissions", {
            "classes": ("wide",),
            "fields": ("groups", "user_permissions"),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(Profile)
admin.site.register(CustomUser, CustomUserAdmin)