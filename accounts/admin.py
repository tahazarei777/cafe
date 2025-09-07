from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # ایمپورت کلاس UserAdmin
from .models import User  # مدل کاربر سفارشی شما

admin.site.register(User, UserAdmin)

  # ثبت مدل با تنظیمات پیش‌فرض ادمین

