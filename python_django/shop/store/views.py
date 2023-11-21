from django.conf import settings
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import Product_Form
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
import os
from django.http import Http404

# Create your views here.

def view_image(request, image_path):
    product = Product.objects.get(image=image_path)
    context = {'product': product, 'image_url': image_path}
    return render(request, 'view_image.html', context)

def home(request):
    cats = Category.objects.all()
    product_data = Product.objects.all()
    p = Paginator(Product.objects.all(), 3)
    page = request.GET.get('page')
    products = p.get_page(page)
    return render(request, 'home_shop.html', {'cats': cats, 'product_data': product_data, 'products': products})


def products(request, cat):
    cats = Category.objects.all()
    product_data = Product.objects.filter(cat__name=cat)
    return render(request, 'products.html', {'cats': cats, "products": product_data, 'cat': cat})


def product(request, cat, id):
    cats = Category.objects.all()
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {'cats': cats, "product": product, 'cat': cat})


def add_product(request):
    if not request.user.groups.filter(name='Create').exists() and not request.user.is_superuser:
        raise Http404
    else:
        cats = Category.objects.all()
        if request.method == 'POST':
            form = Product_Form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # messages.success(request, (f'Product create!! {request.FILES["form.save().image.url}"]}'))
                # return redirect('home')
                new_product = form.save()
                image_path = str(new_product.image)
                image_url = f'/view_image/{image_path}'
                messages.success(request, mark_safe(f'Product created!! <a href="{image_url}" target="_blank">View Image</a>'))
                return redirect('home')
        else:
            form = Product_Form()
        return render(request, 'addproduct.html', {'cats': cats, 'form': form})

def update_product(request, id):
    if not request.user.groups.filter(name='update').exists() and not request.user.is_superuser:
        raise Http404
    else:
        cats = Category.objects.all()
        product = Product.objects.get(pk=id)
        form = Product_Form(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, ('Product update!!!'))
            return redirect ('home')
        return render(request, 'update_product.html', {'cats': cats, 'form': form})

def delete_product(request, id):
    if not request.user.groups.filter(name='Delete').exists() and not request.user.is_superuser:
        raise Http404
    else:
        product = Product.objects.get(pk=id)
        product.delete()
        messages.success(request, ('Product delete!!!'))
        return redirect('home')



# Create your views here.
