from django.db import models
from internalAuth.models import WishitUser

# Create your models here.
class Wishlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default=None, blank=True, null=True)
    owner = models.ForeignKey(WishitUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Wish(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default=None, blank=True, null=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.CharField(max_length=100, default=None, blank=True, null=True)
    count = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title