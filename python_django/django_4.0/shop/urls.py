from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'), # URL для домашньої сторінки, відображає в'юшку home

    path('products/<str:cat>/', views.products, name = 'products')

]