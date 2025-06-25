from django.urls import path
from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<int:product_id>/', views.cart_add, name='card_add'),
    path('cart_change/<int:product_id>/', views.card_change, name='card_change'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]