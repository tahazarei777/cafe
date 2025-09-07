from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import CustomPasswordResetForm, CustomSetPasswordForm

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'registration/password_reset_confirm.html'



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            def save(self, commit=True):
                user = super().save(commit=False)
                user.email = form.cleaned_data['email']  # این خط را اضافه کنید
                user.set_password(self.cleaned_data["password1"])
                if commit:
                    user.save()
                return user
            user = form.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
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
             
            user = authenticate(request=request,username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:  # اگر کاربر سوپریوزر است
                    return redirect('/admin/')  # به پنل ادمین بروید
                else:
                    return redirect('home')  # کاربران عادی به صفحه اصلی
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('home')  # یا هر صفحه‌ای که می‌خواهید
    

