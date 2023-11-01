from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), # URL для домашньої сторінки, відображає в'юшку home

    path('products/<str:cat>/', views.products, name = 'products'),
    path('products/<str:cat>/<int:id>/', views.product, name = 'product'),
    path('add_product/', views.add_product, name = 'add_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),

]