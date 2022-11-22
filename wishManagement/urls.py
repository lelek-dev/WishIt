from django.urls import path, include

from . import views

app_name = "wishlist"
urlpatterns = [
    path('wishlist', views.IndexViewWishlist.as_view(), name='index'),
    # path('wishlist/detail/<int:pk>', views.DetailViewWishlist, name='detail'),
    path('wishlist/create', views.CreateViewWishlist, name='create'),
    path('wishlist/update/<int:pk>', views.UpdateViewWishlist, name='update'),
    path('wishlist/delete/<int:pk>', views.DeleteViewWishlist, name='delete'),
    path('wish/<int:pkWishlist>', views.IndexViewWish, name='indexWish'),
    # path('wish/detail/<int:pkWish>', views.DetailViewWish, name='detailWish'),
    path('wish/create/<int:pkWishlist>', views.CreateViewWish, name='createWish'),
    path('wish/update/<int:pkWish>', views.UpdateViewWish, name='updateWish'),
    path('wish/delete/<int:pkWish>', views.DeleteViewWish, name='deleteWish'),
]