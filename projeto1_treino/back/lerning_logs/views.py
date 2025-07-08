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
from .models import Topic,Entry # importando nossa Classe Topic e Entry de models para criar a view

# lembre-se par acessar arquivos na mesma pasra use o . como no exemplo acima: .models

# lembre-se que o models são as representações das nossas entidades do banco de dados
# com base nisso, fazemos a ligação com o banco de dados, pois o banco está relacionado
# ao model

# Importando método do django que redireciona nossas rotas 
from django.http import HttpResponseRedirect

# Importando o método reverse, basicamente é vai renderizar nossa página apartir de um nome específico de url
from django.urls import reverse

# Importando o nosso formulário criado em forms.py
from .forms import TopicForm, EntryForm

def index(request:HttpRequest)->HttpResponse:
    """Página principal do lerning_log"""
    return render(request, 'lerning_logs/index.html')

# a função render vai renderizar uma página html para o navegador do usuário

# Criando a view topics, função que retorna todos os nossos topicos

def topics(request: HttpRequest)->HttpResponse: # essa função vai retornar um HttpResponse
    """Página que mostra todos os assuntos """
    topics = Topic.objects.order_by('date_added') # ordenando todos os objetos pelas datas adicionadas
    context = {'topics':topics} # crinado contexto que vamos jogar para o template
    return render(request,'lerning_logs/topics.html', context)

# Criando uma view para acessar um tópico específico pela url <-> url dinâmico

def topic(request:HttpRequest,topic_id:str)->HttpResponse:
    """Página que mostra todos os topicos (assuntos) e as anotações referente ao mesmo"""
    topic_id_convertido = int(topic_id) # convertendo o valor da variável vindo da url
    topic = Topic.objects.get(id = topic_id_convertido) # acessando o banco de dados e retornando os dados pelo id
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


# Criando view que irá renderizar o meu formulário criado em form.py
def new_topic(request:HttpRequest)->HttpResponse:
        """ Adiciona um novo Tópico através de um formulário """
                
        if request.method != 'POST':
                # Se nem uma dado for obtido com post; cria-se um formulário em branco
                
                form = TopicForm() # materializando a nossa classe que contém o nosso formulário
        else: 
                form = TopicForm(request.POST) # passando os dados atráves de um endpoint Post
                
                # fazendo validação simples com Django
                if form.is_valid(): # retorna verdadeiro ou false, se os dados forem verdadeiro retorna True se não False
                        form.save() # método utilizado para salvar os dados passados pelo enpoint POST

                        return HttpResponseRedirect(reverse('topics')) # usando o método rever para renderizar uma página apartir do nome de uma url
                        # resumindo essa parte, se os dados enviados via method post for válido e salvar no banco de dados, retornar para a página topics.html 
        
        context = {'form':form}
        return render(request,'lerning_logs/new_topic.html',context,content_type='text/html',status=201)

# Craindo view para o nosso formulário Entryform
def new_annotations(request:HttpRequest,topic_id:str)->HttpResponse:
        """ Acrescenta uma nova anotação no banco de dados """
        topic_id_convertido = int(topic_id)
        topic = Topic.objects.get(id = topic_id_convertido) # acessando o banco de dados e retorndo dados pelo id, veja, você está pegando um objeto do banco de dados 

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
 
# Criando funcionalidade Update para a classe Entry  
def edit_annotations(request: HttpRequest, annotations_id: str) -> HttpResponse:
    """Editar uma anotação existente"""
    
    annotations_id_convertido = int(annotations_id) # coonvertendo o id em inteiro
    annotations = Entry.objects.get(id = annotations_id_convertido) # pegando um objeto do banco de dados com id
    topic = annotations.topic  # Pega o tópico relacionado à anotação

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
    

# CRIANDO NOSSA PÁGINA DE LOGIN
def login(resqust:HttpRequest)->HttpResponse:
        pass