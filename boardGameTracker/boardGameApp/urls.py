from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_protect

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', csrf_protect(LogoutView.as_view(next_page='login')), name='logout'),
    path('library/', views.library_view, name='library'),
    path('add-game/', views.add_game_view, name='add_game'),
    path('game/<str:game_id>/', views.game_details_view, name='game_details'),
    path('game/<str:game_id>/mark-played/', views.mark_as_played_view, name='mark_as_played'),
] 