from django import forms
from .models import UserProfile
from accounts.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'profile_image']
        widgets = {
            'address': forms.Textarea(attrs={'placeholder': 'آدرس  را وارد کنید'}),
        }
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'last_name']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'شماره تلفن را وارد کنید'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل را وارد کنید'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی را وارد کنید'
