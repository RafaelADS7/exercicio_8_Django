from django.shortcuts import render, get_object_or_404
from .models import Filme


def lista_filme(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})


def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    return render(request, 'filmes/detalhe_filme.html', {'filme': filme})
