from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            def save(self, commit=True):
                user = super().save(commit=False)
                user.set_password(self.cleaned_data["password1"])
                if commit:
                    user.save()
                return user
            user = form.save()
            login(request, user) 
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد!') # کاربر را لاگین کن
            return redirect('home')  # به صفحه اصلی برو
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
             
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:  # اگر کاربر سوپریوزر است
                    return redirect('/admin/')  # به پنل ادمین بروید
                else:
                    return redirect('home')  # کاربران عادی به صفحه اصلی
    else:
        form = AuthenticationForm()
        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است!')
    return render(request, 'registration/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('home')  # یا هر صفحه‌ای که می‌خواهید
    