from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import WishitUserCreationForm, WishitUserUpdateForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import WishitUser
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class SignUpView(CreateView):
    form_class = WishitUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def UpdateView(request):
    if request.method == 'POST':
        form = WishitUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('internalAuth:update'))
    else:
        form = WishitUserUpdateForm(instance=request.user)
    return render(request, 'profile/update.html', {'form': form})

def DeleteView(request):
    user = get_object_or_404(WishitUser, pk=request.user.pk)
    user.delete()
    logout(request)
    return HttpResponseRedirect('/')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset/password_reset.html'
    email_template_name = 'password_reset/password_reset_email.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')


# Helper Function
def send_400():
    response = HttpResponse()
    response.status_code = 400              
    return response