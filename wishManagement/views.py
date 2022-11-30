from .models import Wishlist, Wish
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WishForm, WishlistForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Wishlist
class IndexViewWishlist(LoginRequiredMixin, generic.ListView):
    template_name = 'wishlist/index.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        """Return all wishlists."""
        return Wishlist.objects.filter(owner=self.request.user.id)

# def DetailViewWishlist(request, pk):
#     wishlist = get_object_or_404(Wishlist, pk=pk)
#     if wishlist.owner != request.user:
#         send_400()
#     wishes = Wish.objects.filter(wishlist=wishlist.id)
#     return render(request, 'wishlist/detail.html', {'wishlist': wishlist, 'wishes': wishes})

def CreateViewWishlist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WishlistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():                       
            wishlist = Wishlist(title = form.cleaned_data['title'], description = form.cleaned_data['description'], owner = request.user)
            wishlist.save()
            return HttpResponseRedirect(reverse('wishlist:indexWish', args=[wishlist.pk]))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WishlistForm()
    return render(request, 'wishlist/create.html', {'form': form})

def UpdateViewWishlist(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    if wishlist.owner != request.user:
        send_400()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WishlistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():                       
            wishlist.title = form.cleaned_data['title']
            wishlist.description = form.cleaned_data['description']
            wishlist.save()
            return HttpResponseRedirect(reverse('wishlist:indexWish', args=[wishlist.pk]))

    # if a GET (or any other method) we'll create a blank form
    else:        
        form = WishlistForm(instance=wishlist)
    return render(request, 'wishlist/update.html', {'form': form, 'wishlist': wishlist})

def DeleteViewWishlist(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    # if this is a POST request we need to process the form data
    # if request.method == 'DELETE':
    if wishlist.owner == request.user:
        wishlist.delete()
        return HttpResponseRedirect(reverse('wishlist:index'))          
    return send_400()

# Wish
def IndexViewWish(request, pkWishlist):
    wishlist = get_object_or_404(Wishlist, pk=pkWishlist)
    if wishlist.owner != request.user:
        send_400()
    wishes = Wish.objects.filter(wishlist=wishlist.id)
    return render(request, 'wish/index.html', {'wishlist': wishlist, 'wishes': wishes})

# def DetailViewWish(request, pkWish):
#     wish = get_object_or_404(Wish, pk=pkWish)
#     if wish.wishlist.owner != request.user:
#         return send_400()    
#     return render(request, 'wish/detail.html', {'wishlist': wish.wishlist, 'wish': wish})

def CreateViewWish(request, pkWishlist):
    wishlist = get_object_or_404(Wishlist, pk=pkWishlist)
    if wishlist.owner != request.user:
        return send_400() 
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():                   
            wish = Wish(title = form.cleaned_data['title'], description = form.cleaned_data['description'], wishlist = wishlist, product = form.cleaned_data['product'], count = form.cleaned_data['count'])
            wish.save()
            return HttpResponseRedirect(reverse('wishlist:indexWish', args=[wishlist.pk]))
    else:
        form = WishForm()
    return render(request, 'wish/create.html', {'form': form, 'wishlist': wishlist})

def UpdateViewWish(request, pkWish):
    wish = get_object_or_404(Wish, pk=pkWish)
    if wish.wishlist.owner != request.user:
        return send_400()    
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():               
            wish.title = form.cleaned_data['title']
            wish.description = form.cleaned_data['description']
            wish.product = form.cleaned_data['product']
            wish.count = form.cleaned_data['count']
            wish.save()
            return HttpResponseRedirect(reverse('wishlist:indexWish', args=[wish.wishlist.pk]))
    else:
        form = WishForm(instance=wish)
    return render(request, 'wish/update.html', {'form': form, 'wish': wish, 'wishlist': wish.wishlist})

def DeleteViewWish(request, pkWish):
    wish = get_object_or_404(Wish, pk=pkWish)
    if wish.wishlist.owner == request.user:
        wish.delete()
        return HttpResponseRedirect(reverse('wishlist:indexWish', args=[wish.wishlist.pk]))          
    return send_400()

# Helper Function
def send_400():
    response = HttpResponse()
    response.status_code = 400              
    return response