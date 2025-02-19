from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/update/<int:pk>/', views.order_update, name='order_update'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),
]