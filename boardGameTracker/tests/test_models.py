"""
Unit tests for BoardGameTracker models.
"""
from datetime import timedelta, datetime
from typing import Any

import pytest
from django.core.exceptions import ValidationError

from boardGameApp.models import BoardGame, GameStatus, GameType
from tests.factories import BoardGameFactory

pytestmark = pytest.mark.django_db(transaction=True)


def test_board_game_creation_with_valid_data_succeeds(board_game_factory: BoardGameFactory) -> None:
    """
    Test that BoardGame instance can be created with valid data.
    
    Args:
        board_game_factory: Factory for creating test BoardGame instances
    """
    game = board_game_factory.create()
    assert isinstance(game, BoardGame)
    assert game.name.startswith('Test Game')
    assert game.game_type == GameType.MULTIPLAYER
    assert game.last_played is not None


def test_board_game_status_is_normal_when_recently_played(
        board_game_factory: BoardGameFactory,
        current_time: datetime
) -> None:
    """
    Test that game status is NORMAL when played within the last year.
    
    Args:
        board_game_factory: Factory for creating test BoardGame instances
        current_time: Fixed datetime for testing
    """
    recent_date = current_time - timedelta(days=30)
    game = board_game_factory.create(last_played=recent_date)
    assert game.status == GameStatus.NORMAL


def test_board_game_status_is_warning_when_not_played_for_year(
        board_game_factory: BoardGameFactory,
        current_time: datetime
) -> None:
    """
    Test that game status is WARNING when not played for over a year.
    
    Args:
        board_game_factory: Factory for creating test BoardGame instances
        current_time: Fixed datetime for testing
    """
    old_date = current_time - timedelta(days=366)
    game = board_game_factory.create(last_played=old_date)
    assert game.status == GameStatus.WARNING


def test_board_game_status_is_alarm_when_not_played_for_three_years(
        board_game_factory: BoardGameFactory,
        current_time: datetime
) -> None:
    """
    Test that game status is ALARM when not played for over three years.
    
    Args:
        board_game_factory: Factory for creating test BoardGame instances
        current_time: Fixed datetime for testing
    """
    very_old_date = current_time - timedelta(days=3 * 366)
    game = board_game_factory.create(last_played=very_old_date)
    assert game.status == GameStatus.ALARM


def test_board_game_name_cannot_be_empty(board_game_factory: Any) -> None:
    """
    Test that BoardGame cannot be created with an empty name.
    
    Args:
        board_game_factory: Factory for creating test BoardGame instances
    """
    with pytest.raises(ValidationError):
        game = board_game_factory.build(name='')
        game.full_clean()


def test_board_game_last_played_cannot_be_in_future(
        board_game_factory: BoardGameFactory,
        current_time: datetime
) -> None:
    """
    Test that BoardGame cannot have last_played date in the future.
    
    Args:
        board_game_factory: Factory for creating test BoardGame instances
        current_time: Fixed datetime for testing
    """
    future_date = current_time + timedelta(days=1)
    with pytest.raises(ValidationError):
        game = board_game_factory.build(last_played=future_date)
        game.full_clean()


def test_board_game_str_representation(board_game_factory: BoardGameFactory) -> None:
    """
    Test that BoardGame string representation is correct.
    
    Args:
        board_game_factory: Factory for creating test BoardGame instances
    """
    game = board_game_factory.create(name='Monopoly')
    assert str(game) == 'Monopoly (Wieloosobowa)'
