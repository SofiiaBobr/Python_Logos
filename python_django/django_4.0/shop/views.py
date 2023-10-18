from django.shortcuts import render
from .models import Product, Category
# Create your views here.
def home(request):
    cats = Category.objects.all()
    product_data = Product.objects.all()
    return render(request, 'home_shop.html', {'cats': cats, 'products': product_data})

def products(request, cat):
    product_data = Product.objects.filter(cat__name=cat)
    return render(request, 'products.html', {"products": product_data, 'cat': cat})

