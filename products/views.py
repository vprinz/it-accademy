from django.shortcuts import render

from products.models import Product, ProductCategory


# функции = представления = контроллеры

# request = HttpRequest

def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products,
    }
    return render(request, 'products/products.html', context)
