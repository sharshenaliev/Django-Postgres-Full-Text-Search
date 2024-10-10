import factory
from products.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class ProductFactory(factory.django.DjangoModelFactory):
  class Meta:
       model = Product

  name = factory.Faker('name')
  description = factory.Faker('text')
  price = factory.Faker('pyint', min_value=1, max_value=1000)
  category = factory.SubFactory(CategoryFactory)
  image = factory.django.ImageField()
