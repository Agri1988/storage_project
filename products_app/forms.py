from django import forms
from django.contrib.admin import widgets

from .models import Product, Products, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"