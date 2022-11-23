from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'internalAuth'
urlpatterns = [
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("update", views.UpdateView, name="update"),
    path("delete", views.DeleteView, name="delete"),
    path('password-reset', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html', success_url = reverse_lazy('internalAuth:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]