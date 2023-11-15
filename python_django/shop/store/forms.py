from django import forms
from django.forms import ModelForm
from .models import Product

class Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'link', 'cat', 'image')

