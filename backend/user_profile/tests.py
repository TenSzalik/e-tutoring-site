# pylint: disable=unused-argument
import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_superuser():
    admin_user = get_user_model().objects.create_superuser(
        email="super@user.com", password="foobarbaz"
    )
    
    assert admin_user.email == "super@user.com"
    assert admin_user.is_active is True
    assert admin_user.is_staff is True
    assert admin_user.is_superuser is True
    assert admin_user.username is None


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_superuser_without_superuser_flag():
    with pytest.raises(ValueError):
        get_user_model().objects.create_superuser(
            email="super@user.com", password="foobarbaz", is_superuser=False
        )


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_user():
    normal_user = get_user_model().objects.create_user(
        email="normal@user.com", password="foobarbaz"
    )

    assert normal_user.email == "normal@user.com"
    assert normal_user.is_active is True
    assert normal_user.is_staff is False
    assert normal_user.is_superuser is False
    assert normal_user.username is None


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_user_without_required_fields():
    with pytest.raises(TypeError):
        get_user_model().objects.create_user()
    with pytest.raises(TypeError):
        get_user_model().objects.create_user(email="normal@user.com")
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(email="", password="foobarbaz")


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_response_401_if_unauthorized(not_auth_client):
    response = not_auth_client.get("/api/user_profile/")

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_access_succesfully(auth_client):
    response = auth_client.get("/api/user_profile/1/")

    expected_user = {
        "id": 1,
        "first_name": "Gracjan1",
        "last_name": "Chudziak1",
        "email": "test_email@example.com1",
        "password": "foobarbaz1",
    }

    assert response.status_code == status.HTTP_200_OK
    assert expected_user == response.data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_list(auth_client, user):
    response = auth_client.get("/api/user_profile/")
    expected_response = [
        {
            "id": 1,
            "email": "test_email@example.com1",
            "first_name": "Gracjan1",
            "last_name": "Chudziak1",
            "password": "foobarbaz1"
        },
        {
            "id": 2,
            "email": "test_email@example.com2",
            "first_name": "Gracjan2",
            "last_name": "Chudziak2",
            "password": "foobarbaz2"
        },
    ]

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_retrieve(auth_client, user):
    response = auth_client.get("/api/user_profile/1/")
    expected_response = {
        "id": 1,
        "email": "test_email@example.com1",
        "first_name": "Gracjan1",
        "last_name": "Chudziak1",
        "password": "foobarbaz1"
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_create(auth_client, user):
    data = {
        "email": "test_new_email@example.com1",
        "password": "foobarbaz1"
    }

    response = auth_client.post("/api/user_profile/", data, format="json")
    expected_response = {
        "email": "test_new_email@example.com1",
        "password": "foobarbaz1"
    }

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["email"] == expected_response["email"]
    assert response.data["password"] != expected_response["password"]
    assert get_user_model().objects.filter(id=3).exists()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_update(auth_client, user):
    data = {
        "email": "test_email@example.com1",
        "password": "foobarbaz1"
    }
    response = auth_client.put("/api/user_profile/1/", data, format="json")
    expected_response = {
        "email": "test_email@example.com1",
        "password": "foobarbaz1"
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert get_user_model().objects.get(id=1).email == data.get("email")


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_delete(auth_client, user):
    data = auth_client.delete("/api/user_profile/1/")

    assert data.status_code == status.HTTP_204_NO_CONTENT
    with pytest.raises(ObjectDoesNotExist):
        get_user_model().objects.get(id=1)
