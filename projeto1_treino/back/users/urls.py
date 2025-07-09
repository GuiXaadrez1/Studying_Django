from django.urls import path
from django.contrib.auth import views as auth_views # views de autentificação nativa do DJANGO o AS é para apelidar o nome da nossa importação afim de não dar conflito
from . import views 

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html') , name = 'login'), 
    path('logout/', views.logout_view, name='logout'), # essa url vai se referir à saida do nosso login, ou seja, é o deslogar
    path('cadastrar_user',views.cadastro_user, name='cadastro') # lembre que o parâmetro name, é o nome que vamos usar na url dinâmica: {% url 'cadastro' %}
]


'''
    Se colocarmos e deixarmos como um nome padrão, ele vai pra página padrão de login, o npme
    colocado agora será o caminho para o nosso próprio template de login dentro da pasta
    templates/users 
'''