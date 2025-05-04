from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import BoardGame, GameStatus
from datetime import timedelta, datetime
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def page_not_found_view(request, exception):
    """Handle 404 error page."""
    return render(request, 'boardGameTracker/404.html', status=404)

def server_error_view(request):
    """Handle 500 error page."""
    return render(request, 'boardGameTracker/500.html', status=500)

def login_view(request):
    """Handle user login."""
    # If user is already authenticated, redirect to library
    if request.user.is_authenticated:
        return redirect('library')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Witaj, {username}!')
            return redirect('library')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')
    
    return render(request, 'boardGameTracker/login.html')

def register_view(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('library')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Hasła nie są identyczne.')
            return render(request, 'boardGameTracker/register.html')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Użytkownik o takiej nazwie już istnieje.')
            return render(request, 'boardGameTracker/register.html')
            
        try:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            messages.success(request, f'Witaj, {username}! Twoje konto zostało utworzone.')
            return redirect('library')
        except Exception as e:
            messages.error(request, 'Wystąpił błąd podczas tworzenia konta.')
            
    return render(request, 'boardGameTracker/register.html')

@login_required
def library_view(request):
    """Display user's game library."""
    # Get all user's games
    games = request.user.games.all()
    
    # Calculate time thresholds
    now = timezone.now()
    one_year_ago = now - timedelta(days=365)
    three_years_ago = now - timedelta(days=3*365)
    
    # Calculate statistics
    total_games = games.count()
    games_with_alarm = games.filter(last_played__lte=three_years_ago).count()
    games_with_warning = games.filter(
        last_played__lte=one_year_ago,
        last_played__gt=three_years_ago
    ).count()
    
    context = {
        'games': games,
        'now': now,
        'today': now.date(),
        'total_games': total_games,
        'games_with_alarm': games_with_alarm,
        'games_with_warning': games_with_warning,
    }
    return render(request, 'boardGameTracker/library.html', context)

@login_required
def add_game_view(request):
    """Add a new board game to user's collection."""
    if request.method == 'POST':
        name = request.POST.get('name')
        game_type = request.POST.get('game_type')
        last_played = request.POST.get('last_played')

        if not all([name, game_type, last_played]):
            return JsonResponse({
                'success': False,
                'message': 'Wszystkie pola są wymagane.'
            }, status=400)

        try:
            # Convert date string to datetime
            last_played_date = datetime.strptime(last_played, '%Y-%m-%d')
            last_played_datetime = timezone.make_aware(
                datetime.combine(last_played_date, datetime.min.time())
            )

            game = BoardGame.objects.create(
                name=name,
                game_type=game_type,
                last_played=last_played_datetime,
                owner=request.user
            )
            return JsonResponse({
                'success': True,
                'message': f'Gra "{name}" została dodana do twojej kolekcji.',
                'game': {
                    'id': str(game.id),
                    'name': game.name,
                    'game_type': game.game_type,
                    'last_played': game.last_played.strftime('%Y-%m-%d')
                }
            })
        except ValueError as e:
            logger.error(f"ValueError in add_game_view: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': 'Nieprawidłowy format daty.'
            }, status=400)
        except Exception as e:
            logger.error(f"Error in add_game_view: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': 'Wystąpił błąd podczas dodawania gry.'
            }, status=500)

    return JsonResponse({
        'success': False,
        'message': 'Nieprawidłowa metoda żądania.'
    }, status=405)

@login_required
def mark_as_played_view(request, game_id):
    """Mark a game as played today."""
    game = get_object_or_404(BoardGame, id=game_id, owner=request.user)
    game.mark_as_played()
    messages.success(request, f'Gra "{game.name}" została oznaczona jako zagrana dzisiaj.')
    return redirect('game_details', game_id=game_id)

@login_required
def game_details_view(request, game_id):
    """Display detailed information about a specific game."""
    game = get_object_or_404(BoardGame, id=game_id, owner=request.user)
    context = {
        'game': game,
        'now': timezone.now(),
    }
    return render(request, 'boardGameTracker/game_details.html', context)
