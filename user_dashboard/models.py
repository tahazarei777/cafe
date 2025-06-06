from django.db import models
from accounts.models import User  # مدل سفارشی کاربر را ایمپورت کن

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=False, null=True)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    def __str__(self):
        return self.user.username
