import pytest

@pytest.mark.django_db
def test_create_selection(client):
    """
    Тест создания пустой подборки
    """
    data_to_send = {
        "name": "testing selection",
    }

    expected_response = {
        "id": 1,
        "name": "testing selection",
    }

    response = client.post("/selection/create/", data_to_send,
                           content_type="application/json")

    assert response.status_code == 201
    assert response.data == expected_response