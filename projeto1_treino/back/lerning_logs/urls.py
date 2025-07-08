# esse código será responsável pela lógica de roteamento entre as páginas

from django.urls import path
from . import views # o ponto serve para importar métodos, módulos, arquivos de um mesmo diretório

# toda vez que formos criar um path -> manipulação de diretório, vamos colocar um nome para nossa url
urlpatterns = [
    path('',views.index, name = 'index'), # o parâmetro name é o nome da nossa url
    path('topics',views.topics, name='topics'),
    path('topic/<topic_id>/',views.topic, name='topic'), # colocando parâmetro na url para acessae um tópico específico de topics
    path('new_topic', views.new_topic, name = 'new_topic'), # criando caminho para o nosso formulário definido em forms.py que é um CREATE do CRUD
    path('new_annotations/<topic_id>', views.new_annotations, name = 'new_annotations'), # mesma coisa do de cima
    path('edit_annotations/<annotation_id>', views.edit_annotations, name='edit_annotations')
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