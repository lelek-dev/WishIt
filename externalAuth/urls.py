from django.urls import path,include
from . import views

urlpatterns=[
    path('',include('social_django.urls', namespace='externalAuth')),
]