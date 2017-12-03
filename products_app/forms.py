from django import forms

from .models import Product, Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'