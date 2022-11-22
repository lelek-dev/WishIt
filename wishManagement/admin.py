from django.contrib import admin

from .models import Wishlist, Wish

class WishlistAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class WishAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Wish, WishAdmin)