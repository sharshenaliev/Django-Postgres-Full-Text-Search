from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(validators=[MinValueValidator(1), ], verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        indexes = (GinIndex(fields=["search_vector"]),)
