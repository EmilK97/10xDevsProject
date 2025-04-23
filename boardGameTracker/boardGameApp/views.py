from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import BoardGame

# Create your views here.

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
    context = {
        'games': request.user.games.all(),
        'now': timezone.now(),
        'today': timezone.now().date(),
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
            messages.error(request, 'Wszystkie pola są wymagane.')
            return redirect('library')

        try:
            game = BoardGame.objects.create(
                name=name,
                game_type=game_type,
                last_played=last_played,
                owner=request.user
            )
            messages.success(request, f'Gra "{name}" została dodana do twojej kolekcji.')
        except Exception as e:
            messages.error(request, 'Wystąpił błąd podczas dodawania gry.')

        return redirect('library')
    
    return redirect('library')

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
