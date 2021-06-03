from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pw.forms import ContactoForm, ComentarioForm
from pw.models import Contacto

# Create your views here.

def home_page_views(request):
    return render(request, 'pw/home.html')


def eventos_page_views(request):
    return render(request, 'pw/eventos.html')


def feedback_page_views(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('feedback'))
    context = {'form': form}

    return render(request, 'pw/feedback.html', context)


def sobre_page_views(request):
    return render(request, 'pw/sobre.html')


def sobrewebsite_page_views(request):
    return render(request, 'pw/sobreweb.html')


def contactos_view(request):
    if request.user.is_authenticated:
        context = {'contactos': Contacto.objects.all()}
        return render(request, 'pw/contactos.html', context)

    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('contactos'))
    context = {'form': form}

    return render(request, 'pw/contactos.html', context)

def editar_contactos_view(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('contactos'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'pw/editarcontactos.html', context)


def apagar_contactos_view(request, contacto_id):
    Contacto.objects.get(id=contacto_id).delete()
    return HttpResponseRedirect(reverse('contactos'))