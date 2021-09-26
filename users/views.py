from django.shortcuts import redirect, render

# Create your views here.

from django.contrib import messages
from . forms import UserRegisterForm, ProfileUpdate, UserUpdate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)

