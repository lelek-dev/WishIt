from django.urls import path
from . import views
urlpatterns = [
    path("getTypes/<str:search>", views.getTypesView, name="getTypes"),
    path("getOffers", views.getOffersView, name="getOffers"),
]