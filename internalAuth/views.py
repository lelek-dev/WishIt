from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import WishitUserCreationForm, WishitUserUpdateForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import WishitUser

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

# Helper Function
def send_400():
    response = HttpResponse()
    response.status_code = 400              
    return response