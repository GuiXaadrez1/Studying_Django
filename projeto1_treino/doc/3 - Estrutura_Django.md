# Introdução

Esse documento visa explicar como funciona a estrutura inicial que o DJANGO cria ao iniciar um novo projeto! 

# Estrutura dos scripts.py feitas pelos DJANGO:

nome_do_projeto/
├── manage.py   # Script utilitário para interagir com o projeto via linha de comando.
└── nome_do_projeto/
    ├── __init__.py  # Utilizamos para criar módulos e importar o mesmo, deve ser vazia
    ├── settings.py # Arquivo de configuração principal do projeto
    ├── urls.py #  Roteador de caminhos principal do projeto.
    ├── asgi.py # Ponto de entrada assíncrono do projeto (usado por servidores ASGI )
    └── wsgi.py # onto de entrada síncrono do projeto (usado por servidores WSGI)

## menage.py
    
Função: Script utilitário para interagir com o projeto via linha de comando.

O que ele faz:

    Define a variável de ambiente DJANGO_SETTINGS_MODULE com o caminho para o settings.py.

    Chama a função execute_from_command_line(sys.argv) da API do Django para rodar comandos como runserver, migrate, createsuperuser etc.

Exemplo:

    #!/usr/bin/env python
    import os
    import sys

    def main():
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nome_do_projeto.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError("Erro de importação...") from exc
        execute_from_command_line(sys.argv)

    if __name__ == '__main__':
        main()

## __init__.py

Função: Indica que o diretório é um pacote Python.

    Permite que você importe módulos do projeto.

    Normalmente está vazio, mas pode conter inicializações globais.

## settings.py

Função: Arquivo de configuração principal do projeto.

Contém:

    Configurações do Django: INSTALLED_APPS, MIDDLEWARE, TEMPLATES, DATABASES, AUTH_PASSWORD_VALIDATORS

    Localização: LANGUAGE_CODE, TIME_ZONE

    Segurança: SECRET_KEY, DEBUG, ALLOWED_HOSTS

    Caminhos de arquivos estáticos e mídia: STATIC_URL, MEDIA_URL

## urls.py

Função: Roteador principal do projeto.

Define as rotas globais da aplicação.

Usa path() e/ou re_path() para mapear URLs a views.

Exemplo padrão:

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

## asgi.py

Função: Ponto de entrada assíncrono do projeto (usado por servidores ASGI como Daphne/Uvicorn).

Usado para apps reais que requerem WebSocket, comunicação em tempo real etc.

Exmeplo:

    import os
    from django.core.asgi import get_asgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nome_do_projeto.settings')
    application = get_asgi_application()

## wsgi.py

Função: Ponto de entrada síncrono do projeto (usado por servidores WSGI como Gunicorn, uWSGI, etc).

- Usado para deploy tradicional de aplicativos Django.

Exemplo: 

    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nome_do_projeto.settings')
    application = get_wsgi_application()


## Conclusão

manage.py: Entrada para comandos CLI.

settings.py: Cérebro de configurações.

urls.py: Controla rotas globais.

wsgi.py/asgi.py: Entradas para servidores web (síncrono/assíncrono).

__init__.py: Torna o diretório um pacote Python.