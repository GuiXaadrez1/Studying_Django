# Introdução

Esse documento visa deixar registrado a forma como podemos criar rotas em nossas páginas 
html

## EM script urls.py 

Por padrão o DJANGO CRIA ESSA ROTA: 

    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]

Para podermos fazer a navegação entre rotas nas páginas vamos importar os seguintes métodos: path, include.

    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('lerning_logs.urls')) 
    ]

O include serve para organizar e delegar o roteamento de URLs entre diferentes aplicações (apps) dentro de um projeto.

Ao usar include(), você está dizendo:

    “Se a URL começar com esse caminho, passe o controle de roteamento para o arquivo de URLs da app X.”

    Resumindo: path('', include()) quer me dizer o seguinte => se a url for vazia, ir para outro caminho sem ser a página padrão do DJANGO que tem um fuguete, neste caso, vamos para esse arquivo: learning_logs.urls que terá uma url específica.

observação importante: vamos espelhar esse arquivo para dentro da pasta de aplicação, crinado o arquivo urls.py com quase a mesma propriedades, veja! 

app que contém o arquivo urls.py espelhado:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('',views.index),
    ]

não vamos mais precisar do include, pois vamos indicar caminhos e rotas, agora, importamos as nossas views e utilizamos uma função que está dentro de views chamada de index, que é basicamente uma função no script views.py que renderiza a página index.html, que no casso é a nossa página principal. Veja!

from django.shortcuts import render

    def index(request):
        """Página principal do lerning_log"""
        return render(request, 'lerning_logs/index.html')

    - a função render vai renderizar uma página html para o navegador do usuário

Para essa renderização acontecer, vamos ter que criar uma pasta chava para o DJANGO reconhecer chamada de templates, dentro dessa pasta vamos criar uma subpasta chamada: learning_logs e dentro desta subpasta vai esta a nossa página html... o nome da subpasta deve ser a mesma que foi definida no caminho presente na função render()

Para renderizar personalizado, deve-se criar uma pasta específica chamada static ao qual irá comportar todos os nossos CSS