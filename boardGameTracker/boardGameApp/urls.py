from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('library/', views.library_view, name='library'),
    path('add-game/', views.add_game_view, name='add_game'),
    path('game/<str:game_id>/', views.game_details_view, name='game_details'),
    path('game/<str:game_id>/mark-played/', views.mark_as_played_view, name='mark_as_played'),
    path('game/<str:game_id>/delete/', views.delete_game_view, name='delete_game'),
] 