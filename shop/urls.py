from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('category/',views.category, name='category'),
    path('product/',views.product, name='product'),
    path('product/<int:id>/', views.productDetails, name='product_details'),
    path('cart/', views.cart, name='cart'),
]