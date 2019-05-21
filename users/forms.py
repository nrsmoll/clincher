from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Users
        fields = ('username', 'email', 'date_of_birth', 'sex', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('username', 'email', 'date_of_birth', 'sex', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')

