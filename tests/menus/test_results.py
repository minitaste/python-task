from datetime import date

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_today_result_view(auth_client, menu):
    response = auth_client.get("/api/menus/today/results/")

    assert response.status_code == status.HTTP_200_OK
    assert str(response.data["date"]) == str(date.today())
    assert len(response.data["results"]) == 1

    result = response.data["results"][0]
    assert result["restaurant"] == menu.restaurant.name
    assert result["vote_count"] == 0
    assert result["menu"]["breakfast"] == menu.menu_data["breakfast"]
