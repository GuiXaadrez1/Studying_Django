from django.urls import path
from django.contrib.auth import views as auth_views # views de autentificação nativa do DJANGO o AS é para apelidar o nome da nossa importação afim de não dar conflito
from . import views 

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html') , name = 'login'), 
    path('logout/', views.logout_view, name='logout'), # essa url vai se referir à saida do nosso login, ou seja, é o deslogar
    path('cadastro_user',views.cadastro_user, name='cadastro') # lembre que o parâmetro name, é o nome que vamos usar na url dinâmica: {% url 'cadastro' %}
]


'''
    Se colocarmos e deixarmos como um nome padrão, ele vai pra página padrão de login, o nome
    colocado agora será o caminho para o nosso próprio template de login dentro da pasta
    templates/users 

    LoginView
    
        É uma classe genérica baseada em views do Django (django.contrib.auth.views.LoginView).

        Ela já implementa toda a lógica necessária para autenticação de usuários:

        Exibe o formulário de login.

        Verifica se as credenciais estão corretas.

        Faz o login do usuário se tudo estiver certo.    

        
        Configura uma view de login que:

        Usa a lógica pronta de login do Django.

        Renderiza um template customizado (users/login.html) com o formulário de login.

     Parâmetro                     | Descrição                                                                                                                              |
    | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
    | `template_name`               | Caminho para o template HTML que será usado para renderizar o formulário de login.                                                     |
    | `authentication_form`         | Formulário que será usado para autenticação. Por padrão, usa `AuthenticationForm`. Pode ser substituído por um formulário customizado. |
    | `redirect_authenticated_user` | Se `True`, redireciona usuários já autenticados automaticamente (sem mostrar o formulário de login).                                   |
    | `extra_context`               | Dicionário com contexto adicional que será passado para o template.                                                                    |
    | `success_url`                 | URL para redirecionar após o login bem-sucedido (pode ser usado como alternativa ao `next` da URL).                                    |
    | `next_page`                   | Caminho alternativo para redirecionar após o login, se não houver parâmetro `next` na URL.                                             |

    
'''