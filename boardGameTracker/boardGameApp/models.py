from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import string
import random

class GameType(models.TextChoices):
    """
    Enum representing the type of board game.
    Used to distinguish between two-player and multiplayer games.
    """
    TWO_PLAYER = 'TWO', 'Two Player'
    MULTIPLAYER = 'MULTI', 'Multiplayer'

class GameStatus(models.TextChoices):
    """
    Enum representing the status of a board game based on its last played date.
    - NORMAL: Played within the last year
    - WARNING: Not played for over 1 year
    - ALARM: Not played for over 3 years
    """
    NORMAL = 'NORMAL', 'Normal'
    WARNING = 'WARNING', 'Warning'
    ALARM = 'ALARM', 'Alarm'

class UserProfile(models.Model):
    """
    Extension of the built-in Django User model to store additional user-specific data.
    Has a one-to-one relationship with User model.
    """
    # This creates a one-to-one relationship with Django's User model.
    # The User model provides attributes like 'username' automatically.
    # related_name='profile' allows accessing this profile from a user instance via: user.profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # username is a field that exists on Django's built-in User model
        return f"Profile of {self.user.username}"

    @property
    def total_games(self):
        """
        Returns the total number of games in user's collection.
        The 'games' attribute is available because of the related_name='games' in BoardGame.owner field.
        """
        return self.user.games.count()
    
    @property
    def games_with_alerts(self):
        """
        Returns the number of games with ALARM status.
        Uses the same status logic as defined in BoardGame.status property.
        The 'games' attribute is available because of the related_name='games' in BoardGame.owner field.
        """
        three_years_ago = timezone.now() - timedelta(days=3*365)
        return self.user.games.filter(last_played__lte=three_years_ago).count()

    @property
    def games_with_warnings_or_alerts(self):
        """
        Returns the number of games with either WARNING or ALARM status.
        Uses the same status logic as defined in BoardGame.status property.
        The 'games' attribute is available because of the related_name='games' in BoardGame.owner field.
        """
        one_year_ago = timezone.now() - timedelta(days=365)
        return self.user.games.filter(last_played__lte=one_year_ago).count()

class BoardGame(models.Model):
    """
    Represents a board game in a user's collection.
    Tracks game details and automatically computes warning/alert status based on last played date.
    Each game has a unique 8-character ID consisting of random ASCII letters.
    """
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=200)
    # This ForeignKey creates a reverse relation accessible as 'games' on User model
    # because of related_name='games'. This allows queries like user.games.all()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    # Django automatically provides get_game_type_display() method for fields with choices.
    # For example: if game_type is 'TWO', get_game_type_display() returns 'Two Player'
    game_type = models.CharField(
        max_length=5,
        choices=GameType.choices,
        default=GameType.MULTIPLAYER
    )
    last_played = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-last_played']

    def __str__(self):
        return f"{self.name} ({self.get_game_type_display()})"

    @property
    def status(self):
        """
        Computes the current status of the game based on last played date.
        Returns a GameStatus enum value.
        """
        days_since_played = (timezone.now() - self.last_played).days
        
        if days_since_played > 3 * 365:  # 3 years
            return GameStatus.ALARM
        elif days_since_played > 365:  # 1 year
            return GameStatus.WARNING
        return GameStatus.NORMAL

    def mark_as_played(self):
        """Updates the last_played date to now."""
        self.last_played = timezone.now()
        self.save()

    def generate_random_id(self):
        """Generates and sets a random 8-character string ID using ASCII letters."""
        self.id = ''.join(random.choices(string.ascii_letters, k=8))

    def save(self, *args, **kwargs):
        """Override save method to ensure ID is set before saving."""
        if not self.id:
            self.generate_random_id()
        super().save(*args, **kwargs)
