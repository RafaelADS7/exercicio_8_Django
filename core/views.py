from django.shortcuts import render
from .models import Filme

def lista_filme(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})
