# São funções ou classes que respondem às requisições HTTP.

        # módulo
from django.http import HttpRequest, HttpResponse 

# HttpRequest - É a classe que representa a requisição HTTP recebida do navegador.
# Toda vez que um usuário acessa uma página no seu site, Django cria um objeto HttpRequest e o envia para a view correspondente.

# HttpResponse - É a classe que representa a resposta que o Django envia de volta ao navegador.
# Toda view Django deve retornar um HttpResponse (ou um objeto compatível).

        # módulo                # funcao render
from django.shortcuts import render

        # módulo    # Class
from .models import Topic # importando nossa Classe Topic de models para criar a view

# lembre-se par acessar arquivos na mesma pasra use o . como no exemplo acima: .models

# lembre-se que o models são as representações das nossas entidades do banco de dados
# com base nisso, fazemos a ligação com o banco de dados, pois o banco está relacionado
# ao model

def index(request:HttpRequest)->HttpResponse:
    """Página principal do lerning_log"""
    return render(request, 'lerning_logs/index.html')

# a função render vai renderizar uma página html para o navegador do usuário

# Criando a view topics

def topics(request: HttpRequest)->HttpResponse: # essa função vai retornar um HttpResponse
    """Página que mostra todos os assuntos """
    topics = Topic.objects.order_by('date_added') # ordenando todos os objetos pelas datas adicionadas
    context = {'topics':topics} # crinado contexto que vamos jogar para o template
    return render(request,'lerning_logs/topics.html', context)

# Criando uma view para acessar um tópico específico pela url <-> url dinâmico

def topic(request:HttpRequest,topic_id:str)->HttpResponse:
    """Página que mostra todos os topicos (assuntos) e as anotações referente ao mesmo"""
    topic_id_convertido = int(topic_id) # convertendo o valor da variável vindo da url
    topic = Topic.objects.get(id = topic_id_convertido)
    entries = topic.entry_set.order_by('-date_added') # ordenando inversamente
    context = {'topic':topic,'entries':entries} 
    return render(
        request,
        'lerning_logs/topic.html',
        context=context,
        content_type='text/html',
        status=200)

# essa função, view basicamente vai listar um topic com todas as suas anotações com base
# na variável determinada na url
