from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.core.cache import cache
from products.filters import FullSearchFilter
from products.serializers import ProductListSerializer, ProductUpdateSerializer, ProductRetrieveSerializer
from products.models import Product
from django.conf import settings


class ProductViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, OrderingFilter, FullSearchFilter)
    filterset_fields = ('category', )
    ordering = ('-created_at', )

    def get_queryset(self):
        cashed_queryset = cache.get(settings.CACHE_NAME)
        if cashed_queryset:
            queryset = cashed_queryset
        else:
            queryset = Product.objects.select_related("category")
            cache.set(settings.CACHE_NAME, queryset)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductRetrieveSerializer
        else:
            return ProductUpdateSerializer
