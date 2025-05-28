from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    password=forms.CharField(min_length=8, required=False,label="رمز عبور",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')