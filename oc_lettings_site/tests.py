import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_url_root_is_available(client):
    """
    GIVEN a Django application configured for testing
    WHEN the 'index' page is requested (GET)
    THEN check that the response is valid
    """

    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in str(response.content)
