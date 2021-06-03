from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizz_view, name="quizz"),
    path('submit/', views.enviar_tentativa, name="enviar"),
    path('pontuacao/', views.pontuacao_view, name="pontuacao"),
]
