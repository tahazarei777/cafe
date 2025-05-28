from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
import re

class SignUpForm(UserCreationForm):
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
        
        if len(password) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("رمز باید حداقل یک حرف بزرگ داشته باشد")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("رمز باید حداقل یک عدد داشته باشد")
        if all(char.isalnum() for char in password):
            raise forms.ValidationError("رمز باید حداقل یک کاراکتر خاص داشته باشد")
            
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