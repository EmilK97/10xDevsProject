"""
Integration and functional tests for BoardGameTracker.
"""
from typing import Any

import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.utils import timezone

from boardGameApp.models import BoardGame, GameType

pytestmark = pytest.mark.django_db(transaction=True)


# Model Integration Tests
def test_user_can_own_multiple_games(
        user_factory: Any,
        board_game_factory: Any
) -> None:
    """
    Test that a user can own multiple board games.
    
    Args:
        user_factory: Factory for creating test users
        board_game_factory: Factory for creating test board games
    """
    user = user_factory.create()
    games = [
        board_game_factory.create(owner=user, name=f'Game {i}')
        for i in range(3)
    ]

    user_games = BoardGame.objects.filter(owner=user)
    assert user_games.count() == 3
    assert all(game.owner == user for game in user_games)


def test_deleting_user_deletes_their_games(
        user_factory: Any,
        board_game_factory: Any
) -> None:
    """
    Test that deleting a user cascades to delete their games.
    
    Args:
        user_factory: Factory for creating test users
        board_game_factory: Factory for creating test board games
    """
    user = user_factory.create()
    [board_game_factory.create(owner=user) for _ in range(3)]

    assert BoardGame.objects.count() == 3
    user.delete()
    assert BoardGame.objects.count() == 0


# Authentication Tests
def test_user_registration(client: Client) -> None:
    """
    Test user registration process.
    
    Args:
        client: Django test client
    """
    registration_data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'securepass123',
        'password2': 'securepass123'
    }

    response = client.post(reverse('register'), registration_data)
    assert response.status_code == 302  # Redirect after successful registration
    assert User.objects.filter(username='newuser').exists()


def test_user_login_and_logout(client: Client, user_factory: Any) -> None:
    """
    Test user login and logout process.
    
    Args:
        client: Django test client
        user_factory: Factory for creating test users
    """
    user = user_factory.create()

    # Test login
    login_data = {
        'username': user.username,
        'password': 'testpass123'  # Default password from UserFactory
    }
    response = client.post(reverse('login'), login_data)
    assert response.status_code == 302  # Redirect after successful login

    # Test logout
    response = client.post(reverse('logout'))
    assert response.status_code == 302  # Redirect after logout


# Game Management Tests
def test_create_board_game(authenticated_client: Client) -> None:
    """
    Test creating a new board game.
    
    Args:
        authenticated_client: Authenticated Django test client
    """
    game_data = {
        'name': 'New Game',
        'game_type': GameType.MULTIPLAYER,
        'last_played': timezone.now().date()
    }

    response = authenticated_client.post(reverse('add_game'), game_data)
    assert response.status_code == 200
    assert BoardGame.objects.filter(name='New Game').exists()


def test_authorized_access_redirects_to_library(client: Client) -> None:
    """
    Test that authorized access redirects to library.
    
    Args:
        client: Django test client
    """
    response = client.get(reverse('library'))
    assert response.status_code == 302  # Redirect to library
    assert '/library/' in response.url
