from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import WishitUser

class WishitUserCreationForm(UserCreationForm):
    class Meta:
        model = WishitUser
        fields = ("username", "email")
    template_name = "form_snippet.html"
    def __init__(self, *args, **kwargs):
        super(WishitUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'hopefully not visible'

class WishitUserChangeForm(UserChangeForm):
    class Meta:
        model = WishitUser
        fields = ("username", "email")
    template_name = "form_snippet.html"
    def __init__(self, *args, **kwargs):
        super(WishitUserChangeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'hopefully not visible'