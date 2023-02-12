# pylint: disable=unused-argument
import pytest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .models import Tutorial


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_tutorial_list(auth_client, tutorial):
    response = auth_client.get("/api/tutorial/")
    expected_response = [
        {
            "id": 1,
            "name": "course1",
            "date": {"lower": "2023-01-01", "upper": "2024-02-02", "bounds": "[)"},
            "price": 50,
            "description": "Lorem ipsum1",
            "scope": "Lorem ipsum1",
            "lvl": "S",
            "essential": "Lorem ipsum1",
            "learning_form": "Lorem ipsum1",
            "homework": True,
            "status": True,
            "place": [1],
            "support_disabled": [1],
            "premiumtutorial_set": [],
        },
        {
            "id": 2,
            "name": "course2",
            "date": {"lower": "2023-01-01", "upper": "2024-02-02", "bounds": "[)"},
            "price": 50,
            "description": "Lorem ipsum2",
            "scope": "Lorem ipsum2",
            "lvl": "T",
            "essential": "Lorem ipsum2",
            "learning_form": "Lorem ipsum2",
            "homework": True,
            "status": True,
            "place": [1],
            "support_disabled": [1],
            "premiumtutorial_set": [],
        },
    ]

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_tutorial_retrieve(auth_client, tutorial):
    response = auth_client.get("/api/tutorial/1/")
    expected_response = {
        "id": 1,
        "name": "course1",
        "date": {"lower": "2023-01-01", "upper": "2024-02-02", "bounds": "[)"},
        "price": 50,
        "description": "Lorem ipsum1",
        "scope": "Lorem ipsum1",
        "lvl": "S",
        "essential": "Lorem ipsum1",
        "learning_form": "Lorem ipsum1",
        "homework": True,
        "status": True,
        "place": [1],
        "support_disabled": [1],
        "premiumtutorial_set": [],
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_tutorial_create(auth_client, tutorial, disabled):
    data = {
        "name": "course1",
        "date": {
            "lower": "2023-01-01",
            "upper": "2024-02-02",
            "bounds": "[)",
        },
        "price": 50,
        "description": "Lorem ipsum1",
        "scope": "Lorem ipsum1",
        "lvl": "S",
        "essential": "Lorem ipsum1",
        "learning_form": "Lorem ipsum1",
        "homework": False,
        "status": False,
        "place": [1],
        "support_disabled": [2],
    }
    response = auth_client.post("/api/tutorial/", data, format="json")
    expected_response = {
        "id": 3,
        "name": "course1",
        "date": {"lower": "2023-01-01", "upper": "2024-02-02", "bounds": "[)"},
        "price": 50,
        "description": "Lorem ipsum1",
        "scope": "Lorem ipsum1",
        "lvl": "S",
        "essential": "Lorem ipsum1",
        "learning_form": "Lorem ipsum1",
        "homework": False,
        "status": False,
        "place": [1],
        "support_disabled": [2],
    }

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_response
    assert Tutorial.objects.filter(id=3).exists()
    assert Tutorial.objects.filter(date__isempty=False).exists()
    assert Tutorial.objects.filter(date__startswith="2023-01-01").exists()
    assert Tutorial.objects.filter(date__endswith="2024-02-02").exists()
    assert Tutorial.objects.filter(lvl="S").exists()
    assert Tutorial.objects.filter(essential="Lorem ipsum1").exists()
    assert Tutorial.objects.filter(status=False).exists()
    assert Tutorial.objects.filter(place=1).exists()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_tutorial_update(auth_client, tutorial, place, disabled):
    data = {
        "name": "course_updated",
        "date": {
            "lower": "2022-02-02",
            "upper": "2025-01-01",
            "bounds": "[)",
        },
        "price": 60,
        "description": "Lorem ipsum1_updated",
        "scope": "Lorem ipsum1_updated",
        "lvl": "T",
        "essential": "Lorem ipsum1_updated",
        "learning_form": "Lorem ipsum1_updated",
        "homework": True,
        "status": True,
        "place": [2],
        "support_disabled": [2],
    }
    response = auth_client.put("/api/tutorial/1/", data, format="json")
    expected_response = {
        "id": 1,
        "name": "course_updated",
        "date": {
            "lower": "2022-02-02",
            "upper": "2025-01-01",
            "bounds": "[)",
        },
        "price": 60,
        "description": "Lorem ipsum1_updated",
        "scope": "Lorem ipsum1_updated",
        "lvl": "T",
        "essential": "Lorem ipsum1_updated",
        "learning_form": "Lorem ipsum1_updated",
        "homework": True,
        "status": True,
        "place": [2],
        "support_disabled": [2],
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert Tutorial.objects.get(id=1).name == data.get("name")


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_tutorial_delete(auth_client, tutorial):
    data = auth_client.delete("/api/tutorial/1/")

    assert data.status_code == status.HTTP_204_NO_CONTENT
    with pytest.raises(ObjectDoesNotExist):
        Tutorial.objects.get(id=1)
