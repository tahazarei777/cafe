from django.contrib import admin
from . import models
from django.contrib import admin
from django.utils.html import format_html

admin.site.register(models.Category)
# Register your models here.
  # یا هر مدل دیگه‌ای

class ProductAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_link'] = format_html(
            '<a class="button" href="/admin/custom-orders/" target="_blank">مشاهده سفارش‌ها</a>'
        )
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(models.Products, ProductAdmin)
# Register your models here.
