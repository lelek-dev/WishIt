from django.forms import ModelForm, forms
from .models import Wishlist, Wish

class WishlistForm(ModelForm):
    class Meta:
        model=Wishlist
        fields=('title','description')
    template_name = "form_snippet.html"
    def __init__(self, *args, **kwargs):
        super(WishlistForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'hopefully not visible'

class WishForm(ModelForm):
    class Meta:
        model=Wish
        fields=('title','description', 'product', 'count')
    template_name = "form_snippet.html"
    def __init__(self, *args, **kwargs):
        super(WishForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'hopefully not visible'
