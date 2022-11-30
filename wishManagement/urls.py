from django.urls import path, include

from . import views

app_name = "wishlist"
urlpatterns = [
    path('wishlist', views.IndexViewWishlist.as_view(), name='index'),
    path('wishlist/create', views.CreateViewWishlist, name='create'),
    path('wishlist/update/<int:pk>', views.UpdateViewWishlist, name='update'),
    path('wishlist/delete/<int:pk>', views.DeleteViewWishlist, name='delete'),

    path('wish/<int:pkWishlist>', views.IndexViewWish, name='indexWish'),
    path('wish/create/<int:pkWishlist>', views.CreateViewWish, name='createWish'),
    path('wish/update/<int:pkWish>', views.UpdateViewWish, name='updateWish'),
    path('wish/delete/<int:pkWish>', views.DeleteViewWish, name='deleteWish'),

    path('wishlist/share/<uuid:uuidWishlist>', views.ShareViewWishlist, name='share'),

    path('shared', views.IndexViewShared, name='indexShare'),
    path('shared/<int:pkWishlist>', views.DetailViewSharedWishlist, name='detailShareWishlist'),
    path('shared/wish/<int:pkWish>', views.DetailViewSharedWish, name='detailShareWish'),
    path('shared/wish/mark/<int:pkWish>', views.MarkViewSharedWish, name='markShareWish'),
    path('shared/wish/removemark/<int:pkWish>', views.UnmarkViewSharedWish, name='unmarkShareWish'),
]