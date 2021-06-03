from django.contrib import admin

from quizz.models import *
from .models import *

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Comentario)
admin.site.register(Quizz)
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Tentativa)

