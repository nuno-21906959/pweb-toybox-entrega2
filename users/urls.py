from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.home_view, name="users"),
    path('users/login', views.login_view, name="login"),
    path('users/logout', views.logout_view, name="logout"),
    path('users/register', views.register_view, name="register"),
]
