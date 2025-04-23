from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

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
