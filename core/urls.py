from django.urls import path
from . import views
from .views import detalhe_filme

urlpatterns = [
    path('', views.lista_filme, name='lista_filmes'),
    path('filme/<int:filme_id>/', views.detalhe_filme, name='detalhe_filme'),

]
