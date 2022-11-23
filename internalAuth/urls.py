from django.urls import path, include
from . import views

app_name = 'internalAuth'
urlpatterns = [
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("update", views.UpdateView, name="update"),
    path("delete", views.DeleteView, name="delete"),
]