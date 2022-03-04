from rest_framework.viewsets import ModelViewSet

from products.serializers import ProductCategorySerializer
from products.models import ProductCategory


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
