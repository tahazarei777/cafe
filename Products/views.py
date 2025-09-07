from django.shortcuts import render
from .models import Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products, Order, OrderItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order

def admin_order_cards(request):
    orders = Order.objects.select_related('user').prefetch_related('items__product')
    return render(request, 'Admin.html', {'orders': orders})

@csrf_exempt  # برای تست، بعداً بهتره از توکن CSRF محافظت کنی
def delete_order_ajax(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            return JsonResponse({'success': True})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'سفارش یافت نشد'})
    return JsonResponse({'success': False, 'error': 'درخواست نامعتبر'})


@csrf_exempt  
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Products.objects.get(id=product_id)
            # پیدا کردن یا ساخت سفارش جاری کاربر
            order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
            # بررسی اینکه این محصول قبلاً اضافه شده یا نه
            item, item_created = OrderItem.objects.get_or_create(order=order, product=product)
            if not item_created:
                item.quantity += 1
                item.save()
            return JsonResponse({'success': True})
        except Products.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'محصول یافت نشد'})
    return JsonResponse({'success': False, 'error': 'درخواست نامعتبر'})