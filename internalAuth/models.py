from django.contrib.auth.models import AbstractUser

class WishitUser(AbstractUser):
    def __str__(self):
        return self.username