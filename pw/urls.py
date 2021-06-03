from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page_views, name="home"),
    path('eventos', views.eventos_page_views, name="eventos"),
    path('feedback', views.feedback_page_views, name="feedback"),
    path('sobre', views.sobre_page_views, name="sobre"),
    path('sobrewebsite', views.sobrewebsite_page_views, name="sobrewebsite"),
    path('contactos', views.contactos_view, name="contactos"),
    path('contactos/editar/<int:contacto_id>', views.editar_contactos_view, name = "editarcontactos"),
    path('contactos/apagar/<int:contacto_id>', views.apagar_contactos_view, name = "apagarcontactos"),
]
