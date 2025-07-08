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