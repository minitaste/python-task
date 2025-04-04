import pytest
from rest_framework.test import APIClient

from employees.models import Employee


@pytest.mark.django_db
def test_create_employee():
    client = APIClient()

    payload = {
        "username": "admin",
        "password": "1234",
    }

    response = client.post("/api/employees/", payload)

    data = response.data

    assert data["username"] == payload["username"]
    assert "password" not in data
    assert Employee.objects.count() == 1
    assert Employee.objects.get().username == "admin"
