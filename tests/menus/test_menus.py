from datetime import date

import pytest
from rest_framework import status

from menus.models import Menu


@pytest.mark.django_db
def test_create_menu(auth_client, restaurant):

    payload = {
        "date": date.today(),
        "restaurant": restaurant.pk,
        "menu_data": {
            "drink": "Milk",
            "breakfast": "Eggs",
            "lunch": "Burger",
            "dinner": "Fish",
        },
    }

    response = auth_client.post("/api/menus/", payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Menu.objects.count() == 1
    assert Menu.objects.get().date == payload["date"]
    assert Menu.objects.get().menu_data == payload["menu_data"]
    assert Menu.objects.get().restaurant.pk == payload["restaurant"]


@pytest.mark.django_db
def test_create_menu_unauthorized(unauth_client, restaurant):

    payload = {
        "date": date.today(),
        "restaurant": restaurant.pk,
        "menu_data": {
            "drink": "Milk",
            "breakfast": "Eggs",
            "lunch": "Burger",
            "dinner": "Fish",
        },
    }

    response = unauth_client.post("/api/menus/", payload, format="json")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Menu.objects.count() == 0
