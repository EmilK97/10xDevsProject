"""
Test factories for BoardGameTracker models using factory_boy.
"""
from datetime import datetime, timezone
from typing import Any

import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from boardGameApp.models import BoardGame, GameType


class UserFactory(DjangoModelFactory):
    """Factory for creating test User instances."""

    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: f'test_user_{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')


class BoardGameFactory(DjangoModelFactory):
    """Factory for creating test BoardGame instances."""

    class Meta:
        model = BoardGame
        django_get_or_create = ('name', 'owner')

    name = factory.Sequence(lambda n: f'Test Game {n}')
    owner = factory.SubFactory(UserFactory)
    game_type = GameType.MULTIPLAYER
    last_played = factory.LazyFunction(lambda: datetime.now(timezone.utc))

    @factory.post_generation
    def set_custom_last_played(self, create: bool, extracted: Any, **kwargs: Any) -> None:
        """
        Post-generation hook to set custom last_played date if provided.
        
        Args:
            create: Whether the model instance is being created
            extracted: The value passed to the factory
            **kwargs: Additional keyword arguments
        """
        if not create:
            return

        if extracted:
            self.last_played = extracted
            self.save()
