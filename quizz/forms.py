from django import forms
from django.forms import ModelForm

from quizz.models import Quizz, Pergunta
from django.db import models

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

class PerguntaForm:
    class Meta:
        model = Quizz
        fields = '__all__'
