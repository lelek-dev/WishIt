from django.db import models
from internalAuth.models import WishitUser

# Create your models here.
class Wishlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(WishitUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Wish(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    count = models.IntegerField()
    def __str__(self):
        return self.title