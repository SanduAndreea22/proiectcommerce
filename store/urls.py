from . import views
from django.urls import path

urlpatterns = [
    path('', views.store, name='store'),
    path('perfum_info/<slug:slug>/', views.perfum_info, name='perfum-info'),
    path('cart/', views.cart_summary, name='cart-summary'),
    path('add/<int:id>/', views.cart_add, name='cart-add'),
    path('delete/<int:id>/', views.cart_delete, name='cart-delete'),
    path('update/<int:id>/', views.cart_update, name='cart-update'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('order-success/', views.order_success, name='order-success'),
    path('register/', views.register, name='register'),
    path('my-login/', views.my_login, name='my-login'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('track-orders/', views.track_orders, name='track-orders'),
]


