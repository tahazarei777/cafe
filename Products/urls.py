from django.urls import path
from .views import admin_order_cards,delete_order_ajax,add_to_cart

urlpatterns = [
    path('admin/orders/', admin_order_cards, name='admin_order_cards'),
    path('admin/orders/delete/', delete_order_ajax, name='delete_order_ajax'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),

]