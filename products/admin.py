from django.contrib import admin

from products.models import ProductCategory, Product

admin.site.register(Product)
admin.site.register(ProductCategory)
