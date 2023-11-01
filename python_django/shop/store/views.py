from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import Product_Form
from django.contrib import messages
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
            messages.success(request, ('Product create!!!'))
            return redirect('home')
    else:
        form = Product_Form()
    return render(request, 'addproduct.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(pk=id)
    form = Product_Form(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, ('Product update!!!'))
        return redirect ('home')
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request, ('Product delete!!!'))
    return redirect('home')



# Create your views here.
