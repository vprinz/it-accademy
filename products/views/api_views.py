from rest_framework.viewsets import ModelViewSet

from products.serializers import ProductCategorySerializer, ProductSerializer
from products.models import ProductCategory, Product


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
