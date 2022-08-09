import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


def fake_create():

    fake_user = User(username="Moriarti")
    fake_user.save()
    fake_user.set_password("none")
    fake_user.save()

    fake_profile = Profile(
        user=fake_user,
        favorite_city="Paris"
    )
    fake_profile.save()
    return fake_user, fake_profile


@pytest.mark.django_db
def test_url_profiles_index_is_available(client):
    """
    GIVEN a Django application configured for testing
    WHEN the 'index' page of the profile app is requested (GET)
    THEN check that the response is valid
    """

    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Profiles</title>" in str(response.content)


@pytest.mark.django_db
def test_url_profiles_profile_is_available(client):
    """
    GIVEN a Django application configured for testing
    WHEN the 'detail' page of one profile is requested (GET)
    THEN check that the response is valid
    """
    fake_user, fake_profile = fake_create()
    # print("fake_profile", fake_profile)
    # print("fake_user", fake_user)
    url = reverse("profiles:profile",  args=[fake_profile.user])
    response = client.get(url, data={})
    assert response.status_code == 200
    assert "Paris" in str(response.content)
