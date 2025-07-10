# Introdução
Impedindo que usários acessem outros tópicos que não são os dele

## Primeiro vamos filtrar com a função filter() todos os objetos de um tópico

@login_required
def topics(request: HttpRequest)->HttpResponse: # essa função vai retornar um HttpResponse
    """Página que mostra todos os assuntos """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # ordenando todos os objetos pelas datas adicionadas
    context = {'topics':topics} # crinado contexto que vamos jogar para o template
    return render(request,'lerning_logs/topics.html', context)

    - Isso não é suficiente, porque o usuário pode acessar asa informações de outros usuários através da url dinâmica: 'topic/<topic_id>/',

## Impedindo os usuários acessar outras informações pela URL dinâmica, preste atenção no IF e ELSE

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Topic,Entry 
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404 # Classe nativa do Django que renderiza uma página 404


@login_required
def topics(request: HttpRequest)->HttpResponse: # essa função vai retornar um HttpResponse
    """Página que mostra todos os assuntos """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # ordenando todos os objetos pelas datas adicionadas
    # filter() função que vai filtrar todos os topicos pelo seu respectivo dono
    context = {'topics':topics} # crinado contexto que vamos jogar para o template
    return render(request,'lerning_logs/topics.html', context)

@login_required
def topic(request:HttpRequest,topic_id:str)->HttpResponse:
    """Página que mostra todos os topicos (assuntos) e as anotações referente ao mesmo"""
    topic_id_convertido = int(topic_id) # convertendo o valor da variável vindo da url
    topic = Topic.objects.get(id = topic_id_convertido) # acessando o banco de dados e retornando os dados pelo id
    
    # fazendo validação com if e else que impede outros usuários acessar informações que não são os deles pelo html dinâmico
    # Garante que o topico, assunto pertence ao usuário atual
    
    if topic.owner != request.user:
        raise Http404 # redireciona para uma página 404 padrão do DJANGO
    
    entries = topic.entry_set.order_by('-date_added') # ordenando inversamente
    context = {'topic':topic,'entries':entries} 
    return render(
        request,
        'lerning_logs/topic.html',
        context=context,
        content_type='text/html',
        status=200)


@login_required
def new_topic(request:HttpRequest)->HttpResponse:
        """ Adiciona um novo Tópico através de um formulário """
                
        if request.method != 'POST':
                # Se nem uma dado for obtido com post; cria-se um formulário em branco
                
                form = TopicForm() # materializando a nossa classe que contém o nosso formulário
        else: 
                form = TopicForm(request.POST) # passando os dados atráves de um endpoint Post
                
                # fazendo validação simples com Django
                if form.is_valid(): # retorna verdadeiro ou false, se os dados forem verdadeiro retorna True se não False
                        
                        new_topic = form.save(commit=False) # salva como um objeto, mas não no banco de dados
                        new_topic.owner = request.user # usuário atual vai ser salvo na fk de topic, lembre-se que esse cara está em CASCADE
                        new_topic.save() # método utilizado para salvar os dados passados pelo enpoint POST no banco de dados

                        return HttpResponseRedirect(reverse('topics')) # usando o método rever para renderizar uma página apartir do nome de uma url
                        # resumindo essa parte, se os dados enviados via method post for válido e salvar no banco de dados, retornar para a página topics.html 
        
        context = {'form':form}
        return render(request,'lerning_logs/new_topic.html',context,content_type='text/html',status=201)

@login_required
def new_annotations(request:HttpRequest,topic_id:str)->HttpResponse:
        """ Acrescenta uma nova anotação no banco de dados """
        topic_id_convertido = int(topic_id)
        topic = Topic.objects.get(id = topic_id_convertido) # acessando o banco de dados e retorndo dados pelo id, veja, você está pegando um objeto do banco de dados 

        if topic.owner != request.user:
                raise Http404 # redireciona para uma página 404 padrão do DJANGO
        
        if request.method != 'POST':
                # nenhum dado submetido, então retorna uma formulário em branco
                form = EntryForm()
        else:
                # dados submetidos, processa os dados
                form = EntryForm(data=request.POST) # NÃO PEGA todos os dados da requisição, apenas alguns dados 
                
                if form.is_valid():
                        
                        # criando um objeto form para fazer validação
                        new_annotation = form.save(commit=False) # salva os dados enviados via POST para o banco de dados

                        # o parâmetro commit = false serve para salvar os dados em um objeto e não diretamente no banco de dados
                        
                        new_annotation.topic = topic # acrescentando um novo atributo, chamado topic ao objeto new_annotation que é um topic adquirido pelo banco de dados
                        
                        # agora sim vamos fazer um save de fato, inserir, persistir os dados dentro do banco de dados!

                        new_annotation.save()
        
                        return HttpResponseRedirect(reverse('topic',args=[topic_id_convertido])) # após validações redirecionar para página topic e passando como argumento da url o id
        
        context = {'topic':topic,'form':form}
        return render(
                request,
                'lerning_logs/new_annotations.html',
                context=context,content_type='text/html',
                status=200)
 
@login_required
def edit_annotations(request: HttpRequest, annotations_id: str) -> HttpResponse:
    """Editar uma anotação existente"""
    
    annotations_id_convertido = int(annotations_id) # coonvertendo o id em inteiro
    annotations = Entry.objects.get(id = annotations_id_convertido) # pegando um objeto do banco de dados com id
    topic = annotations.topic  # Pega o tópico relacionado à anotação
        
    if topic.owner != request.user:
        raise Http404
  
    if request.method != "POST":
        form = EntryForm(instance=annotations)  # Formulário pré-preenchido com os dados atuais
    else:
        # se os formulário for um método POST, logo será atualizado os dados
        form = EntryForm(instance=annotations, data=request.POST) # pegando os dados preenchidos e atualizando com os dados enviados pela requisição POST
         # validando dados adiquiridos pelo formulário
        if form.is_valid(): 
            form.save() # salva dentro do banco de dados
            return HttpResponseRedirect(reverse('topic', args=[topic.id])) # após validações redirecionar para página topic e passando como argumento da url e o id do topic
 
    context = {'annotations':annotations,'topic':topic,'form':form}
    return render ( 
            request,
            'lerning_logs/edit_annotations.html',
            context= context, # constroi a página conforme os dados passado no dicinário de dados, icionário com dados para passar ao template (`{{ var }}` no HTML)
            content_type='text/html',
            status=200
    )


## Modificando a view new_topic para quando um usuario criar um novo topico, esse novo topico criado seja atribuido a ele