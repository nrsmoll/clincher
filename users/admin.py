# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Users

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    list_display = ['username', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']
    fieldsets = (
        (('User'), {'fields': ('username', 'email',  'password', 'sex', 'date_of_birth',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff')}),
    )

admin.site.register(Users, CustomUserAdmin)