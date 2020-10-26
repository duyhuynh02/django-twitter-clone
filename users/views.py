from django.urls import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, FormView

from .models import Profile 
from .forms import (
    CustomUserCreationForm, 
    ProfileUpdateForm, 
    CustomUserUpdateForm,
)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


@login_required
def settings(request):
    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('twitter')
    else:
        user_form = CustomUserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profile_update.html', context)