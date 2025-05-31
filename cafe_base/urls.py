
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from accounts import views
from accounts.views import CustomPasswordResetView, CustomPasswordResetConfirmView
urlpatterns = [
    path('',include('cafe_app1.urls')),
    path(" ",include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('accounts.urls')),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
