from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import WishitUser

class WishitUserCreationForm(UserCreationForm):
    class Meta:
        model = WishitUser
        fields = ("username", "email")

class WishitUserChangeForm(UserChangeForm):
    class Meta:
        model = WishitUser
        fields = ("username", "email")