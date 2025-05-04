"""
Functional tests for BoardGameTracker focusing on end-to-end flows.
"""
from typing import Any

import pytest
from django.test import Client
from django.urls import reverse

from boardGameApp.models import BoardGame, GameType, GameStatus
from tests.factories import UserFactory

pytestmark = pytest.mark.django_db(transaction=True)


def test_complete_registration_and_login_flow(client: Client) -> None:
    """
    Test the complete user registration and login flow.
    
    Args:
        client: Django test client
    """
    # 1. User visits registration page
    response = client.get(reverse('register'))
    assert response.status_code == 200

    # 2. User submits registration form
    registration_data = {
        'username': 'newplayer',
        'email': 'player@example.com',
        'password1': 'securepass123',
        'password2': 'securepass123'
    }
    response = client.post(reverse('register'), registration_data)
    assert response.status_code == 302  # Redirect after registration

    # 3. User logs out (should be automatically logged in after registration)
    response = client.post(reverse('logout'))
    assert response.status_code == 302

    # 4. User logs in with new credentials
    login_data = {
        'username': 'newplayer',
        'password': 'securepass123'
    }
    response = client.post(reverse('login'), login_data)
    assert response.status_code == 302
    assert response.url == reverse('library')  # Should redirect to library


def test_complete_game_management_flow(
        authenticated_client: Client,
        current_time: Any
) -> None:
    """
    Test the complete flow of managing a board game.
    
    Args:
        authenticated_client: Authenticated Django test client
        current_time: Current datetime fixture
    """
    # 1. User adds a new game
    game_data = {
        'name': 'Catan',
        'game_type': GameType.MULTIPLAYER,
        'last_played': current_time.date()
    }
    response = authenticated_client.post(reverse('add_game'), game_data)
    assert response.status_code == 200

    game = BoardGame.objects.get(name='Catan')
    assert game.status == GameStatus.NORMAL

    # 2. User views the game in their library
    response = authenticated_client.get(reverse('library'))
    assert response.status_code == 200
    assert 'Catan' in str(response.content)
