from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Resposta(models.Model):
    resposta_text = models.CharField(max_length=900)
    is_correct = models.BooleanField(default=False)


class Pergunta(models.Model):
    pergunta_text = models.CharField(max_length=900)
    resposta = models.ManyToManyField(Resposta)
    pontos = models.PositiveIntegerField()


class Quizz(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    nr_tentativas = models.PositiveIntegerField()
    tempo_limite_mins = models.PositiveIntegerField()
    perguntas = models.ManyToManyField(Pergunta)


class Tentativa(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    pontos = models.PositiveIntegerField(default=0)
    entrega = models.DateTimeField(auto_now_add=True)

