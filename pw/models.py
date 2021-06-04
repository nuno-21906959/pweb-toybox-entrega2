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

COMENTARIO_CHOICES = [
    (1, 'PÉSSIMO'),
    (2, 'MAU'),
    (3, 'BOM'),
    (4, 'MUITO BOM'),
    (5, 'EXCELENTE'),
]
class Comentario(models.Model):
    clareza = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    rigor = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    precisao = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    profundidade = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    amplitude = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    logica = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    significancia = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    originalidade = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)

