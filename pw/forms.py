import datetime

from django.forms import ModelForm

from . import models
from .models import Contacto, Comentario
from django import forms


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'