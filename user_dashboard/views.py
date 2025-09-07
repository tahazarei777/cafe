from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm, UserUpdateForm
from .models import UserProfile

@login_required
def edit_profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "لطفاً ابتدا وارد حساب شوید.")
        return redirect('login')

    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST" and request.POST.get("delete_image"):
        if user_profile.profile_image:
            user_profile.profile_image.delete(save=True)
            messages.success(request, "تصویر پروفایل شما حذف شد.")
        return redirect('profile')

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            lat = request.POST.get('lat')
            lng = request.POST.get('lng')
            
            if lat and lng:
                try:
                    request.user.latitude = float(lat)
                    request.user.longitude = float(lng)
                except ValueError:
                    messages.warning(request, "مختصات معتبر نیست.")

            user_form.save()
            user_profile.save()
            request.user.save()
            messages.success(request, "تغییرات با موفقیت ذخیره شد.")
            print(lat)
            print(lng)
            return redirect('home')
        else:
            messages.error(request, "اطلاعات وارد‌شده معتبر نیست.")
    else:
        profile_form = UserProfileForm(instance=user_profile)
        user_form = UserUpdateForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {
        'profile_form': profile_form,
        'user_form': user_form,
        'user_profile': user_profile,
    })
