from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('questions/', views.questions),
    path('recording/', views.recording),
    path('leaderboard/', views.leader_board),
    path('gameover/', views.game_over),
]