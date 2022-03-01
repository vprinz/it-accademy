from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),  # ../products/
    path('category/<int:category_id>/', products, name='category'),  # .../products/category/1/
]
