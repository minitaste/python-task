from datetime import date

import pytest
from rest_framework import status

from menus.models import Menu
from restaurants.models import Restaurant


@pytest.mark.django_db
def test_today_menu_view(auth_client, menu):
    response = auth_client.get("/api/menus/today/")

    assert response.status_code == status.HTTP_200_OK

    result = response.data["results"]
    assert len(result) == 1
    assert result[0]["restaurant"] == menu.restaurant.id
    assert result[0]["menu_data"]["lunch"] == "Pasta"


@pytest.mark.django_db
def test_today_menu_unauthorized(unauth_client):
    response = unauth_client.get("/api/menus/today/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
