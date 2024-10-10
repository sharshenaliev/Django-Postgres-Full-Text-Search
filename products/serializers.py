from rest_framework import serializers
from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        exclude = ('search_vector', 'description')


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('search_vector', 'created_at')


class ProductRetrieveSerializer(ProductListSerializer):

    class Meta:
        model = Product
        exclude = ('search_vector',)
