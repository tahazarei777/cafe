from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from .models import User
import re
from django.core.exceptions import ValidationError

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("لطفاً ایمیل خود را وارد کنید.")
        
        if not self.get_users(email):
            raise ValidationError("این ایمیل در سیستم ثبت نشده است.")
        return email

class CustomSetPasswordForm(SetPasswordForm):
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('new_password1')
        
        if password:
            errors = []
            
            # 1. حداقل ۸ کاراکتر
            if len(password) < 8:
                errors.append("رمز عبور باید حداقل ۸ کاراکتر باشد.")
            
            # 2. حداقل یک حرف بزرگ
            if not any(char.isupper() for char in password):
                errors.append("رمز عبور باید حداقل یک حرف بزرگ داشته باشد.")
            
            # 3. حداقل یک عدد
            if not any(char.isdigit() for char in password):
                errors.append("رمز عبور باید حداقل یک عدد داشته باشد.")
            
            # 4. حداقل یک نماد خاص
            if all(char.isalnum() for char in password):
                errors.append("رمز عبور باید حداقل یک نماد خاص داشته باشد.")
            
            if errors:
                raise ValidationError(errors)
        
        return cleaned_data

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)
    phone = forms.CharField(
        max_length=11,
        min_length=11,
        required=True,
        label="شماره تلفن",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '09xxxxxxxxx',
            'pattern': '09\d{9}',
            'title': 'شماره تلفن باید با 09 شروع شود و 11 رقم باشد'
        })
    )
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.startswith('09'):
            raise forms.ValidationError("شماره تلفن باید با 09 شروع شود")
        return phone
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        if password:
            errors = []
            
            if len(password) < 8:
                errors.append("رمز عبور باید حداقل 8 کاراکتر باشد")
            if not any(char.isupper() for char in password):
                errors.append("رمز باید حداقل یک حرف بزرگ داشته باشد")
            if not any(char.isdigit() for char in password):
                errors.append("رمز باید حداقل یک عدد داشته باشد")
            if all(char.isalnum() for char in password):
                errors.append("رمز باید حداقل یک کاراکتر خاص داشته باشد")
            
            if errors:
                raise forms.ValidationError(errors)
            
        return password
    
    password2 = None
    
    class Meta:
        model = User
        fields = ('username', 'phone', 'password1')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'نام کاربری',
            'password1': 'رمز عبور',
        }