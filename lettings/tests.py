import pytest
from django.urls import reverse

from .models import Address, Letting


def fake_create():
    fake_address = Address(
        number=121,
        street="Baker Street",
        city="London",
        state="BR",
        zip_code=9999,
        country_iso_code="UK"
    )
    fake_address.save()
    fake_letting = Letting(
        title="Rent of Doctor Watson",
        address=fake_address
    )
    fake_letting.save()
    return fake_address, fake_letting


@pytest.mark.django_db
def test_url_lettings_index_is_available(client):
    """
    GIVEN a Django application configured for testing
    WHEN the 'index' page of the letting app is requested (GET)
    THEN check that the response is valid
    """

    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Lettings</title>" in str(response.content)


@pytest.mark.django_db
def test_url_lettings_letting_is_available(client):
    """
    GIVEN a Django application configured for testing
    WHEN the 'detail' page of one letting is requested (GET)
    THEN check that the response is valid
    """
    fake_address, fake_letting = fake_create()
    print("fake_letting.id", fake_letting.id)
    url = reverse("lettings:letting",  args=[fake_letting.id])
    response = client.get(url, data={})
    assert response.status_code == 200
    assert "Rent of Doctor Watson" in str(response.content)
