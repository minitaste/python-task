import pytest
from rest_framework import status

from restaurants.models import Restaurant


@pytest.mark.django_db
def test_create_restaurant(auth_client):

    payload = {"name": "Test Restaurant", "address": "123 Test Street"}

    response = auth_client.post("/api/restaurants/", payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.count() == 1
    assert Restaurant.objects.get().name == "Test Restaurant"
    assert Restaurant.objects.get().address == "123 Test Street"


def test_create_restaurant_unauthorizate(unauth_client):
    payload = {"name": "Test Restaurant", "address": "123 Test Street"}

    response = unauth_client.post("/api/restaurants/", payload, format="json")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
