from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_products.as_view(), name="base"),
    path('',views.home.as_view(),name="home"),
    path('admin/custom-orders/', views.orders_admin_view, name='orders_admin_view'),
]