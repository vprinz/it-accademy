from django.shortcuts import render


# функции = представления = контроллеры

# request = HttpRequest

def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'price': 6090,
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
            },
            {
                'name': 'Синяя куртка The North Face',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'price': 23725,
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'price': 3390,
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
            },
        ]
    }
    return render(request, 'products/products.html', context)
