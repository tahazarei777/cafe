from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from . models import UserProfile
from django.contrib import messages
from django.shortcuts import redirect

def redirect_to_login(request):
    messages.warning(request, "لطفاً ابتدا وارد حساب کاربری خود شوید تا بتوانید به داشبورد دسترسی داشته باشید.")
    return redirect('login')

def edit_profile(request):
    if not request.user.is_authenticated:  # بررسی ورود کاربر
        messages.warning(request, "لطفاً ابتدا وارد حساب شوید تا بتوانید به داشبورد دسترسی داشته باشید.")
        return redirect('login')
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)

            if not user.last_name:
                user.last_name = ""

            user.save()
            profile_form.save()

        return redirect('home')

    else:
        profile_form = UserProfileForm(instance=user_profile)
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'edit_profile.html', {
        'profile_form': profile_form, 
        'user_form': user_form
    })

