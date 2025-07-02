# esse código será responsável pela lógica de roteamento entre as páginas

from django.urls import path
from . import views

# toda vez que formos criar um path -> manipulação de diretório, vamos colocar um nome para nossa url
urlpatterns = [
    path('',views.index, name = 'index'), # o parâmetro name é o nome da nossa url
    path('topics',views.topics, name='topics'),
    path('topic/<topic_id>/',views.topic, name='topic') # colocando parâmetro na url para ser acessada
]

'''
    Vamos analisar detalhadamente os parâmetros da função path() dentro da lista urlpatterns

    path(route, view, kwargs=None, name=None)

    | Parâmetro | Descrição Técnica                                                                  |
    | --------- | ---------------------------------------------------------------------------------- |
    | `route`   | URL que será reconhecida pelo navegador. É o “caminho” depois do domínio.          |
    | `view`    | Função ou classe que será executada ao acessar essa rota.                          |
    | `kwargs`  | (opcional) Dicionário com parâmetros adicionais passados para a view.              |
    | `name`    | (opcional) Nome simbólico da rota, usado para gerar URLs dinâmicas com `{% url %}` |

    Explicação do caminho de url no route:
    
    path('topics', views.topics, name='topics')
    
    'topics': representa o caminho /topics (ou seja, http://localhost:8000/topics)

    views.topics: view que será executada para essa rota

    name='topics': você pode gerar essa URL no HTML assim:
    
        <a href="{% url 'topics' %}">Ver Tópicos</a>

'''