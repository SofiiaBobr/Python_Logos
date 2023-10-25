from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import Product_Form
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    cats = Category.objects.all()
    product_data = Product.objects.all()
    return render(request, 'home_shop.html', {'cats': cats, 'products': product_data})

def products(request, cat):
    product_data = Product.objects.filter(cat__name=cat)
    return render(request, 'products.html', {"products": product_data, 'cat': cat})

def product(request, cat, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {"product": product, 'cat': cat})

def add_product(request):
    if request.method == 'POST':
        form = Product_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Product_Form()
    return render(request, 'addproduct.html', {'form': form})
