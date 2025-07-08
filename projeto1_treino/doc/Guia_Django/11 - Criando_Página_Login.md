# INTRODUÇÃO
Esse documento tem como objetivo explicar como fazer umna página de login com DJNAGO

## Usuários do DJANGO
Podemos utilizar a tabela de usuário do próprio DJANGO, vamos criar uma nova aplicação como exemplo
use o comando:

    python manage.py startapp users

Cadastre um admin novo - use o comando: python manage.py createsuperuser

vai retonar algo como:

  Username (leave blank to use 'guigui'): não é obrigado a colocar, (colocar o usuario do windows no login)
  Email address: não é obrigado a colocar
  Password: é obrigado a colocar (senha que eu coloquei: 123456789)

após: 

  Password (again): 
  This password is too common.
  This password is entirely numeric.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.

## Painel administrativo do DJANGO 

    Pelo painel administrativo podemos adicionar novos usuários com seus devidos atributos e permissões 
    lá no campo ou opção users

    A senha do Django já é salva em formato HASH

    AUTHENTICATION AND AUTHORIZATION -> basicamente é o nível de acesso que permite o usuário acessar as páginas que precisam da autentificação


## Criando estrutura de templates para nossa página login

    dentro de templates vamos criar uma sub pasta chamda users que irá conter o nosso html login


## Criando view nativa para criar nossa tela login.

Dentro do nosso scripts urls.py que criamos dentro do nosso projeto de aplicação users, vamos colocar o seguinte código:

    from django.urls import path
    #import views
    from django.contrib.auth import views as auth_views # views de autentificação nativa do DJANGO o AS é para apelidar o nome da nossa importação afim de não dar conflito


    urlpatterns = [
        path('login', auth_views.LoginView.as_view(template_name='users/login.html') , name = 'login') 
    ]


    '''
        Se colocarmos e deixarmos como um nome padrão, ele vai pra página padrão de login, o npme
        colocado agora será o caminho para o nosso próprio template de login dentro da pasta
        templates/users 
    '''

## No nosso template html dentro da subpasta users:

    {% extends "lerning_logs/base.html" %}

    {% block content %}

        {% if forms.erros %}
            <p>Seu login e senha estão incorretos! Por favor, tente novamente.</p>
        {% endif %}

        <form action="{% url 'login' %}" method="post">
            {% csrf_token %}
            {{form.as_p}}
            <button name = "submit">Entrar</button>
        </form>

    {%  endblock content %}

## Sobre o login Padrão do Django:  from django.contrib.auth import views as auth_views, LoginView.as_view(template_name='users/login.')

- Importação

    from django.contrib.auth import views as auth_views

- O que isso faz?

    Importa o módulo views do app django.contrib.auth.

    Renomeia esse módulo para auth_views localmente.

    Isso é feito para evitar conflitos com possíveis views suas chamadas views.py.

- Por que views as auth_views?

    Você pode ter um arquivo views.py no seu app. Para não colidir com django.contrib.auth.views, o uso de as auth_views torna a importação mais clara e segura:

    auth_views.LoginView  # referência explícita à view de login do Django

- View baseada em classe: LoginView

    auth_views.LoginView.as_view(template_name='users/login.html')

O que isso faz?
    
    LoginView é uma classe baseada em view (CBV) fornecida pelo Django para lidar com autenticação de usuários.

    O método as_view() transforma essa classe em uma função de view que pode ser chamada pelo Django quando um usuário acessa a URL /login.

    O argumento template_name='users/login.html' sobrescreve o template padrão que o Django usaria (registration/login.html), e instrui a view a renderizar o seu próprio arquivo users/login.html.

- O que o LoginView espera?

    A view de login do Django:

    Usa um formulário padrão chamado AuthenticationForm.

    Espera um POST com os campos username e password.

    Espera que o template definido tenha esse formulário renderizado, normalmente assim:

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>

Se o login for bem-sucedido:

    Redireciona para settings.LOGIN_REDIRECT_URL (por padrão: /accounts/profile/), a menos que você sobrescreva esse comportamento.

## Configurando o settings.py para redirecionar quando o login for bem sucedido

No seu settings.py, adicione a seguinte configuração para indicar para onde o usuário deve ser redirecionado após o login:

LOGIN_REDIRECT_URL = '/'

Ou, por exemplo, se quiser redirecionar para a lista de tópicos:

LOGIN_REDIRECT_URL = '/topics'

Isso resolve o erro sem precisar criar uma nova view.


#  Se quiser controlar o redirecionamento dinamicamente?

Você pode usar o parâmetro next no login:

<form action="{% url 'login' %}?next=/topics" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>

lembrando que tudo após o ? é uma requisição GET


# O Django reconhece next como o campo que informa para qual URL o usuário deve ser redirecionado após o login.

Se você omitir esse campo, ele usa a configuração:

LOGIN_REDIRECT_URL = '/accounts/profile/'

Como você já configurou:

LOGIN_REDIRECT_URL = '/topics'

Você só precisa usar next se quiser redirecionar dinamicamente para uma URL específica, como a página inicial (index).