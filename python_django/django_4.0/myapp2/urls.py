from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'), # URL для домашньої сторінки, відображає в'юшку home
    path('main/', views.main, name = 'mane') # URL для головної сторінки, відображає в'юшку main
]

