"""
Pytest configuration and fixtures for BoardGameTracker tests.
"""
from datetime import datetime, timezone
from typing import Any

import pytest
from django.test import Client
from pytest_factoryboy import register

from tests.factories import UserFactory, BoardGameFactory

# Register factories
register(UserFactory)
register(BoardGameFactory)


@pytest.fixture
def authenticated_client(client: Client, user_factory: Any) -> Client:
    """
    Returns an authenticated client with a test user.
    
    Args:
        client: Django test client
        user_factory: Factory for creating test users
        
    Returns:
        Client: Authenticated Django test client
    """
    user = user_factory.create()
    client.force_login(user)
    return client


@pytest.fixture
def current_time() -> datetime:
    """
    Returns the current datetime in UTC.
    This ensures tests are always using fresh timestamps.
    
    Returns:
        datetime: Current UTC datetime
    """
    return datetime.now(timezone.utc)
