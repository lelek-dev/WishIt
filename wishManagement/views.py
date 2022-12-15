from .models import Wishlist, Wish, userConnectWishlist, WishMarks
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

def CreateViewWishlist(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():                       
            wishlist = Wishlist(title = form.cleaned_data['title'], description = form.cleaned_data['description'], owner = request.user)
            wishlist.save()
            return HttpResponseRedirect(reverse('wishlist:indexWish', args=[wishlist.pk]))
    else:
        form = WishlistForm()
    return render(request, 'wishlist/create.html', {'form': form})

def UpdateViewWishlist(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    if wishlist.owner != request.user:
        send_400()
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():                       
            wishlist.title = form.cleaned_data['title']
            wishlist.description = form.cleaned_data['description']
            wishlist.save()
            return HttpResponseRedirect(reverse('wishlist:indexWish', args=[wishlist.pk]))
    else:        
        form = WishlistForm(instance=wishlist)
    return render(request, 'wishlist/update.html', {'form': form, 'wishlist': wishlist})

def DeleteViewWishlist(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    if wishlist.owner == request.user:
        wishlist.delete()
        return HttpResponseRedirect(reverse('wishlist:index'))          
    return send_400()

# Wish
def IndexViewWish(request, pkWishlist):
    wishlist = get_object_or_404(Wishlist, pk=pkWishlist)
    if wishlist.owner != request.user:
        return send_400()
    wishes = Wish.objects.filter(wishlist=wishlist.id)
    return render(request, 'wish/index.html', {'wishlist': wishlist, 'wishes': wishes})

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

# Share
def ShareViewWishlist(request, uuidWishlist):
    wishlist = get_object_or_404(Wishlist, uuid = uuidWishlist)
    if wishlist.owner != request.user:
        if not userConnectWishlist.objects.filter(user_id = request.user, wishlist_id = wishlist).exists():
            userConnectVar = userConnectWishlist(user_id = request.user, wishlist_id = wishlist)
            userConnectVar.save()
    return HttpResponseRedirect(reverse('wishlist:detailShareWishlist', args=[wishlist.pk])) 

def IndexViewShared(request):
    shared_list = userConnectWishlist.objects.values_list('wishlist_id', flat=True).filter(user_id = request.user)
    wishlists = Wishlist.objects.filter(pk__in=shared_list)
    marked_list = WishMarks.objects.values_list('wish_id', flat=True).filter(user_id = request.user)
    wishes = Wish.objects.filter(pk__in=marked_list)
    return render(request, 'shared/index.html', {'wishlists': wishlists, 'wishes': wishes})

def DetailViewSharedWishlist(request, pkWishlist):
    wishlist = get_object_or_404(Wishlist, pk=pkWishlist)
    if not userConnectWishlist.objects.filter(user_id = request.user, wishlist_id = pkWishlist).exists():
        send_400(403)
    wishes = Wish.objects.filter(wishlist=wishlist.id)
    return render(request, 'shared/detailWishlist.html', {'wishlist': wishlist, 'wishes': wishes})
    
def DetailViewSharedWish(request, pkWish):
    wish = get_object_or_404(Wish, pk=pkWish)
    if not userConnectWishlist.objects.filter(user_id = request.user, wishlist_id = wish.wishlist.pk).exists():
        send_400(403)    
    return render(request, 'shared/detailWish.html', {'wish': wish, 'wishlist': wish.wishlist})

def MarkViewSharedWish(request, pkWish):
    wish = get_object_or_404(Wish, pk=pkWish)
    if not userConnectWishlist.objects.filter(user_id = request.user, wishlist_id = wish.wishlist.pk).exists():
        send_400(403)   
    mark = WishMarks(user_id = request.user, wish_id = wish)
    mark.save()
    return HttpResponseRedirect(reverse('wishlist:detailShareWishlist', args=[wish.wishlist.pk]))

def UnmarkViewSharedWish(request, pkWish):
    wish = get_object_or_404(Wish, pk=pkWish)
    mark = get_object_or_404(WishMarks, wish_id = wish.pk)
    # actor can be owner or marker of list
    if not (request.user == mark.user_id or request.user == wish.wishlist.owner):
        send_400(403)   
    mark.delete()
    return render(request, 'shared/detailWish.html', {'wish': wish, 'wishlist': wish.wishlist})

# Helper Function
def send_400(code = 400):
    response = HttpResponse()
    response.status_code = code              
    return response