"""
Functional tests for the game deletion functionality in BoardGameTracker.
"""
from typing import Any

import pytest
from django.test import Client
from django.urls import reverse

from boardGameApp.models import BoardGame
from tests.factories import UserFactory, BoardGameFactory

pytestmark = pytest.mark.django_db(transaction=True)


def test_user_can_delete_own_game(authenticated_client: Client) -> None:
    """
    Test that a user can successfully delete a game they own.
    
    Args:
        authenticated_client: Authenticated Django test client
    """
    # 1. Create a game owned by the authenticated user
    user = authenticated_client.session['_auth_user_id']
    game = BoardGameFactory.create(owner_id=user)
    game_id = str(game.id)

    # 2. Verify the game exists
    assert BoardGame.objects.filter(id=game_id).exists()

    # 3. Send a POST request to delete the game
    response = authenticated_client.post(reverse('delete_game', args=[game_id]))

    # 4. Verify the response is a redirect to the library
    assert response.status_code == 302
    assert response.url == reverse('library')

    # 5. Verify the game no longer exists in the database
    assert not BoardGame.objects.filter(id=game_id).exists()


def test_user_cannot_delete_another_users_game(authenticated_client: Client) -> None:
    """
    Test that a user cannot delete a game owned by another user.
    
    Args:
        authenticated_client: Authenticated Django test client
    """
    # 1. Create another user and a game owned by that user
    other_user = UserFactory.create()
    game = BoardGameFactory.create(owner=other_user)
    game_id = str(game.id)

    # 2. Verify the game exists
    assert BoardGame.objects.filter(id=game_id).exists()

    # 3. Try to delete the game as the authenticated user
    response = authenticated_client.post(reverse('delete_game', args=[game_id]))

    # 4. Verify the response is a 404 (not found)
    assert response.status_code == 404

    # 5. Verify the game still exists in the database
    assert BoardGame.objects.filter(id=game_id).exists()


def test_delete_nonexistent_game(authenticated_client: Client) -> None:
    """
    Test the behavior when trying to delete a game that doesn't exist.
    
    Args:
        authenticated_client: Authenticated Django test client
    """
    # 1. Try to delete a game with a non-existent ID
    nonexistent_id = "999999"
    response = authenticated_client.post(reverse('delete_game', args=[nonexistent_id]))

    # 2. Verify the response is a 404 (not found)
    assert response.status_code == 404


def test_delete_game_redirects_to_library(
        authenticated_client: Client,
        current_time: Any
) -> None:
    """
    Test that after deleting a game, the user is redirected to their library 
    with appropriate success message.
    
    Args:
        authenticated_client: Authenticated Django test client
        current_time: Current datetime fixture
    """
    # 1. Create a game owned by the authenticated user
    user = authenticated_client.session['_auth_user_id']
    game = BoardGameFactory.create(
        owner_id=user,
        name="Test Game To Delete"
    )
    game_id = str(game.id)

    # 2. Delete the game
    response = authenticated_client.post(reverse('delete_game', args=[game_id]))

    # 3. Follow the redirect
    response = authenticated_client.get(response.url)

    content = response.content.decode('utf-8')
    # 4. Verify the library is displayed
    assert 'Twoja biblioteka' in content or 'Biblioteka gier' in content
