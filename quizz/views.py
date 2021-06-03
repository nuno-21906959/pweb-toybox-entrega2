from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from quizz.models import Quizz, Pergunta, Tentativa, Resposta
from .utils import get_plot
from datetime import datetime


# Create your views here.

def quizz_view(request):
    context = {'quizzes': Quizz.objects.all(), 'perguntas': Pergunta.objects.all()}
    return render(request, 'quizz.html', context)

    form = QuizzForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(''))
    context = {'form': form}

    return render(request, 'quizz.html', context)


def enviar_tentativa(request):
    user = request.user
    pontos = 0
    quizz_id = request.POST.get('quizz_id')
    quizz = Quizz.objects.get(id=quizz_id)
    r1 = int(request.POST.get('1'))
    r2 = int(request.POST.get('2'))
    r3 = int(request.POST.get('3'))
    r4 = int(request.POST.get('4'))
    r5 = int(request.POST.get('5'))
    r6 = int(request.POST.get('6'))

    if request.method == 'POST':
        pontos = r1+r2+r3+r4+r5+r6


    t = Tentativa.objects.create(
        quizz=quizz,
        pessoa=user,
        pontos=pontos
    )

    t.save()
    return redirect('home')

def pontuacao_view(request):
    user = request.user
    quizzes = Quizz.objects.all()
    tentativas = Tentativa.objects.all()
    count = 0

    for tentativa in tentativas:
        if tentativa.pessoa == user:
            count +=1

    x = [x.entrega.strftime("%d-%m-%Y, %H:%M:%S") for x in tentativas if x.pessoa == user]
    y = [y.pontos for y in tentativas if y.pessoa == user]

    chart = get_plot(x, y)
    context = {'quizzes': quizzes, 'tentativas': tentativas, 'chart': chart, 'count': count}
    return render(request, 'pontuacao.html', context)