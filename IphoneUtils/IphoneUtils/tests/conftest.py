import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.fixture
def auth_user():
    user = User.objects.create(username='test_user')
    user.set_password('test_password')
    return user

@pytest.fixture
def auth_token(auth_user):
    token, create = Token.objects.get_or_create(user=auth_user)
    return token


@pytest.fixture
def api_client(auth_user, auth_token):
    client = APIClient()
    client.force_authenticate(user=auth_user, token=auth_token)
    return client