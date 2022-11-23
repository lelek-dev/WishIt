from django.forms import ModelForm
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

class WishitUserUpdateForm(UserChangeForm):
    class Meta:
        model = WishitUser
        fields = ("username", "email")
    template_name = "form_snippet.html"
    def __init__(self, *args, **kwargs):
        super(WishitUserUpdateForm, self).__init__(*args, **kwargs)
        del self.fields['password']
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'hopefully not visible'

class WishitUserForm(ModelForm):
    class Meta:
        model=WishitUser
        fields=('username','email')
    template_name = "form_snippet.html"
    def __init__(self, *args, **kwargs):
        super(WishitUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'hopefully not visible'