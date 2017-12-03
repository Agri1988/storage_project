from django.contrib import admin

from products_app.models import Product, Products, ProductMovement, Category


admin.site.register(Product)
admin.site.register(Products)
admin.site.register(ProductMovement)
admin.site.register(Category)
