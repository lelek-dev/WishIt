from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import WishitUserCreationForm, WishitUserChangeForm
from .models import WishitUser

class WishitUserAdmin(UserAdmin):
    add_form = WishitUserCreationForm
    form = WishitUserChangeForm
    model = WishitUser
    list_display = ["email", "username",]

admin.site.register(WishitUser, WishitUserAdmin)