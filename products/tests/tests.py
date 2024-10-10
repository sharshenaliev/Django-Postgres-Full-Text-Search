import pytest
from django.conf import settings
import pytz
from faker import Faker
from pytest_factoryboy import register
from products.tests.factories import ProductFactory, CategoryFactory


register(CategoryFactory)
register(ProductFactory)


@pytest.mark.django_db
def test_product_list(client, product):
    response = client.get('/api/v1/products/')
    data = response.data['results'][0]
    assert response.status_code == 200
    assert response.data['count'] == 1
    assert product.name == data['name']


@pytest.mark.django_db
def test_product_post(client, category):
    product = ProductFactory.build()
    data = {
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "category": category.id,
        "image": product.image,
    }
    response = client.post("/api/v1/products/", data=data)
    assert response.status_code == 201
    assert response.data['name'] == data['name']
    assert response.data['description'] == data['description']
    assert response.data['price'] == data['price']


@pytest.mark.django_db
def test_product_get(client, product):
    response = client.get(f"/api/v1/products/{product.id}/")
    assert response.status_code == 200
    assert (response.data['created_at'] == product.created_at.
            astimezone(pytz.timezone(settings.TIME_ZONE)).strftime("%Y-%m-%d %H:%M:%S"))
    assert response.data['category'] == {'id': product.category.id, 'name': product.category.name}
    assert response.data['image'] == f"http://testserver{product.image.url}"


@pytest.mark.django_db
def test_product_patch(client, product):
    new_name = Faker().name()
    print(new_name)
    data = {"name": new_name}
    response = client.patch(f"/api/v1/products/{product.id}/", data=data, content_type='application/json')
    assert response.status_code == 200
    assert response.data['name'] != product.name
    assert response.data['name'] == new_name


@pytest.mark.django_db
def test_product_delete(client, product):
    response = client.delete(f"/api/v1/products/{product.id}/")
    assert response.status_code == 204
