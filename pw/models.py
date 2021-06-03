from django.db import models
from django import forms
from django.forms import NumberInput

# Create your models here.


class Contacto(models.Model):
    nome = models.CharField(max_length=15)
    apelido = models.CharField(max_length=15)
    datanasc = models.DateField()
    telefone = models.TextField(max_length=9)
    email = models.EmailField(max_length=40)
    mensagem = models.TextField(max_length=500)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Contacto de: " + self.nome[:15] + " " + self.apelido[:15] + " [" + self.criado.strftime(
            "%d-%m-%Y") + "]"



class Comentario(models.Model):
    clareza = models.IntegerField()
    rigor = models.IntegerField()
    precisao = models.IntegerField()
    profundidade = models.IntegerField()
    amplitude = models.IntegerField()
    logica = models.IntegerField()
    significancia = models.IntegerField()
    originalidade = models.IntegerField()
