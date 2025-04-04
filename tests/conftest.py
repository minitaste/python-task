from datetime import date

import pytest
from rest_framework.test import APIClient

from employees.models import Employee
from menus.models import Menu
from restaurants.models import Restaurant


@pytest.fixture
def employee(db):
    return Employee.objects.create_user(username="testuser", password="password123")


@pytest.fixture
def auth_client(employee):
    client = APIClient()
    response = client.post(
        "/api/token/",
        {"username": "testuser", "password": "password123"},
        format="json",
    )
    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client


@pytest.fixture
def unauth_client():
    return APIClient()


@pytest.fixture
def restaurant():
    return Restaurant.objects.create(name="Testaurant", address="Test Street")


@pytest.fixture
def menu(restaurant):
    return Menu.objects.create(
        date=date.today(),
        restaurant=restaurant,
        menu_data={
            "drink": "Juice",
            "breakfast": "Eggs",
            "lunch": "Pasta",
            "dinner": "Salmon",
        },
    )


@pytest.fixture
def voter():
    return Employee.objects.create_user(username="voter", password="pass")


@pytest.fixture
def vote(menu, voter):
    from menus.models import Vote

    return Vote.objects.create(employee=voter, menu=menu)
