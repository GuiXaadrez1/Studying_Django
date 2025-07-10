# Introdução
Esse documento tem como objetivo mostrar uma forma de vincular a cada usuário os seus proprios assuntos, anotações, sem ver informações de outros usuários, vir url ou outras formas
ou seja, vamos trazer privacidade, cada topico, anotação pertence a um usuário em específico, ninguem pode ver as mesmas coisas ou ter acesso a informações de outros usuários a não ser que este ja um administrador.

## Primiero, vamos modificar os nossos models

from django.db import models
from django.contrib.auth.models import User # importando Class usuário, nativa do próprio Django

## Crie os seus Models (Entidades do Banco de dados) aqui

class Topic(models.Model): # fazendo uma herança 
    
    # definindo um atributo que será do tipo CharField com no máximo 200 caracteres, basicamente representa o nosso VARCHAR(200)
    text = models.CharField(max_length=200) 
    
    # definindo um atributo da nossa classe que vai automaticamente adicionar data e hora do nosso computador neste campo
    date_added = models.DateTimeField(auto_now_add=True)
    
    # vinculando um dono a um tópico em específico
    owner =  models.ForeignKey(User, on_delete=models.CASCADE) # Materializando o nosso usuário nativo como uma FK
    
    # crinado o nosso contrutor (opcional, não é obrigatório)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # atributo especial que chama o construtor da class pai
    
    '''
        Anotações sobre *args e **kwargs
        
        *args:
            
            É uma convenção, não uma palavra reservada do Python 
            (você poderia usar outro nome, mas é padrão usar args).

            O asterisco * significa: receber um número variável de argumentos 
            posicionais como uma tupla.

        **kwargs:
            
            Também uma convenção (significa “keyword arguments”).

            O ** significa: receber um número variável de argumentos nomeados 
            (chave=valor) como um dicionário.
    
    '''

## Abrir o prompt de comando do DJANGO

tanto no powershell
tanto no cmd

python mange.py shell

## Identificando usuário

Dentro do nosso shell do DJANGO, vamos pesquisar o id dos topicos e vincular cada id a foreign key do USER:

    from django.contrib.auth.models import User
    User.obejects.all()

    vai retornar algo como:

    >>> from django.contrib.auth.models import User
    >>> User.objects.all()
    <QuerySet [<User: guigui>, <User: aluno>, <User: guilherme>]>

    # para descobrir o nome e o id do usuário
    >>> for user in User.objects.all():
        print(user.username,user.id) 
    
    após descobrir qual é o usuário, vamos sair da shell com exit()

## Criar migrations
    use o comando: python manage.py makemigrations lerning_logs(nome da aplicação)

    esse comando vai criar as nossas migrações 

    após isso você vai resceber duas opções:

    (.venv) PS C:\Studying_Django\projeto1_treino\back>  python manage.py makemigrations lerning_logs
    It is impossible to add a non-nullable field 'owner' to topic without specifying a default. This is because the database needs something to populate existing rows.
    Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit and manually define a default value in models.py.
    Select an option:                                              

    primeira opção: permite que o Django faça as modificações nos valores já existentes na models porém, colocando dados com valor padrão nesta  models modificada
    segunda opção: permite que você faça manualmente as migrações na Models 

    -> Optei por escolher a primeira opção

    Após isso ele pergunta para você o seguinte: Qual é o valor que você gostaria de colocar naquele campo modificado, no nosso caso é uma FK por ID

    -> Optei por escolher o numero inteiro 3

    vai retronar o seguinte valor:

    Migrations for 'lerning_logs':
    lerning_logs\migrations\0004_topic_owner.py
        + Add field owner to topic
    (.venv) PS C:\Studying_Django\projeto1_treino\back> 

    Agora você vai usar o seguinte comando: 

        python manage.py migrate

    esse comando vai realizar de fato a migration, alteração no banco de dados

    Ele vai retornar o seguinte:

        (.venv) PS C:\Studying_Django\projeto1_treino\back> python manage.py migrate
        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, lerning_logs, sessions
        Running migrations:
        Applying lerning_logs.0004_topic_owner... OK
        (.venv) PS C:\Studying_Django\projeto1_treino\back> 


## Verificando se as alterações foram feitas pelo próprio shell do nativo do python pelo DJANGO

    >>> from lerning_logs.models import Topic
    >>> for topic in Topic.objects.all():
    ...     print(topic.owner, topic.text)   