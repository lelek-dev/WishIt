from django.urls import path, include

from . import views

urlpatterns = [
    path('wishlist/', views.IndexView.as_view(), name='index'),
    path('wishlist/<int:pk>/', views.DetailView.as_view(), name='detail'),
]

