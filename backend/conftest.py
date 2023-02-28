import pytest
from model_bakery import baker, seq
from model_bakery.recipe import Recipe
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

custom_user = Recipe(
    get_user_model(),
    email=seq("test_email@example.com"),
    password=seq("foobarbaz"),
    first_name=seq("Gracjan"),
    last_name=seq("Chudziak"),
)

@pytest.fixture(name="user")
def fixture_user():
    return custom_user.make(_quantity=2)


@pytest.fixture(name="not_auth_client")
def fixture_not_auth_client() -> APIClient:
    client = APIClient()
    return client


@pytest.fixture(name="auth_client")
def fixture_auth_client(user) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user[0])
    return client


@pytest.fixture(name="place")
def fixture_place():
    baker.make_recipe("common.custom_place", _quantity=2)


@pytest.fixture(name="disabled")
def fixture_disabled():
    baker.make_recipe("common.custom_disabled", _quantity=2)


@pytest.fixture(name="tutorial")
def fixture_tutorial():
    baker.make_recipe("tutorial.custom_tutorial", _quantity=2)
