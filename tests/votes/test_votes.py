import pytest
from rest_framework import status

from datetime import date
from menus.models import Vote

@pytest.mark.django_db
def test_vote_create(auth_client, restaurant, menu):

    response = auth_client.post("/api/votes/", {"menu": menu.id}, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Vote.objects.count() == 1

    response = auth_client.post("/api/votes/", {"menu": menu.id}, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
