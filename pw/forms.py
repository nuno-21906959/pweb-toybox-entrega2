import datetime

from django.forms import ModelForm, DateInput

from . import models
from .models import Contacto, Comentario
from django import forms


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'datanasc': DateInput(attrs={'type': 'date'})
        }

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
