from .models import Wishlist, Wish
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'wishlist/index.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        """Return all wishlists."""
        return Wishlist.objects.filter(owner=self.request.user.id)

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Wishlist
    template_name = 'wishlist/detail.html'