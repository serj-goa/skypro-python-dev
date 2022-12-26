import pytest

@pytest.mark.django_db
def test_retrieve_ad(client, ad, admin_token):
    """
    Выдача одного объявления
    """
    expected_response = {
        "id": ad.pk,
        "category": None,
        "author": None,
        "name": "testing name",
        "price": 100,
        "description": "testing description",
        "is_published": False,
        "image": None
    }

    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer " + admin_token)

    assert response.status_code == 200
    assert response.data == expected_response