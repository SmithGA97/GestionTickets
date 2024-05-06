from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import pytest
from django.test import Client
from django.contrib.auth.models import User
from tickets.models import Ticket


@pytest.fixture
def create_user_fixture(db):
    def _create_user(username, password, email):
        user = User.objects.create_user(username=username, password=password, email=email)
        return user
    return _create_user

@pytest.fixture
def user_with_token_fixture(db):
    user = User.objects.create_user(username='testuser', password='password123')
    token = Token.objects.create(user=user)
    return user, token.key

@pytest.mark.django_db
def test_create_ticket(user_with_token_fixture):
    user, token_key = user_with_token_fixture
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {token_key}')
    response = client.post('/tickets/', {
        "tittle" : "Photos about nature",
        "number_of_images": 5,
        "description" : "nature pics",
        }
    )
    assert response.status_code == 201
    assert Ticket.objects.filter(tittle='Photos about nature').exists()

@pytest.mark.django_db
def test_get_token(create_user_fixture):
    user = create_user_fixture('testuser', 'password123', 'smithgaspri_od@gmail.com')
    client = Client()
    assert user.username == 'testuser'
    response = client.post('/token/', {
            "username": "testuser",
            "password": "password123"
        }
    )
    assert response.status_code == 200
