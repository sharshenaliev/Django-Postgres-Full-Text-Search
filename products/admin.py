from django.contrib import admin
from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('search_vector',)
    list_display = ('name', 'price')
    ordering = ('price', )


admin.site.register(Category)
