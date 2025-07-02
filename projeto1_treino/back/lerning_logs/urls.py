# esse código será responsável pela lógica de roteamento entre as páginas

from django.urls import path
from . import views

# toda vez que formos criar um path -> manipulação de diretório, vamos colocar um nome para nossa url
urlpatterns = [
    path('',views.index, name = 'index'), # o parâmetro name é o nome da nossa url
]