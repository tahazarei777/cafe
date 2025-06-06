from django.urls import path
from .views import edit_profile, redirect_to_login

urlpatterns = [
    path('edit/', edit_profile, name='edit_profile'),
    path('login_required/', redirect_to_login, name='login_required'),
]
