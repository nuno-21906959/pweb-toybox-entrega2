from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.posts_index, name="spa-index"),
    path("posts/", views.posts, name="spa-posts"),
]