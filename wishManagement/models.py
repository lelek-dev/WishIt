from django.db import models
import uuid
from internalAuth.models import WishitUser

# Create your models here.
class Wishlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default=None, blank=True, null=True)
    owner = models.ForeignKey(WishitUser, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def viewers(self):
        return userConnectWishlist.objects.filter(wishlist_id=self.pk).exists()

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
    def marked(self):
        return WishMarks.objects.filter(wish_id=self.pk).exists()

class userConnectWishlist(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(default=None, blank=True, null=True)
    user_id = models.ForeignKey(WishitUser, on_delete=models.CASCADE)
    wishlist_id = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class WishMarks(models.Model):
    wish_id = models.ForeignKey(Wish, on_delete=models.CASCADE)
    user_id = models.ForeignKey(WishitUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.wish_id