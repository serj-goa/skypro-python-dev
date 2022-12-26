import pytest


@pytest.mark.django_db
def test_create_ad_1(client):
    """
    Тест успешного создание объявления
    """
    data_to_send = {
        "name": "Котики-обормотики",
        "price": 0,
        "description": "веселые котики",
        "is_published": False
    }
    expected_response = {
        "id": 11,
        "author": None,
        "category": None,
        "name": "Котики-обормотики",
        "price": 0,
        "description": "веселые котики",
        "is_published": False,
        "image": None
    }
    response = client.post("/ad/create/", data_to_send, content_type='application/json')

    assert response.status_code == 201
    assert response.data == expected_response

def test_create_ad_2(client):
    """
    Тест валидации имени объявления при создании
    """
    data_to_send = {
        "name": "Жулик",
        "price": 1000,
        "description": "Хитрый жулики, жульничают",
        "is_published": False
    }
    expected_response = {
        "name": ["Ensure this field has at least 10 characters."]
    }

    response = client.post("/ad/create/", data_to_send, content_type='application/json')

    assert response.status_code == 400
    assert response.data == expected_response
