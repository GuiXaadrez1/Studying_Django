# INTRODUÇÃO

    essa documentação visa explicar de forma suncinta e fácil como funcina o painel administrtivo do DJANGO

## cadastrando um administrador:

use o comando: python manage.py createsuperuser

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

## colocando as entidades, tabelas para aparecerem:

no script admin.py da aplicação vamos importar nossa Class e registrar com um método específico.

Exemplo:

    from django.contrib import admin
    from lerning_logs.models import Topic # importando da pasta da nossa aplicação do arquivo models a Class Topic

    # Registre o seu Model aqui

    admin.site.register(Topic) # Registrando a nossa Class Topic


## Funcionalidades do Painel administrativo

Com o Django Admin, é possível:

- Visualizar todas as tabelas (models) registradas

- Criar, editar, excluir registros (CRUD completo)

- Gerenciar dados sem escrever SQL manualmente

- Usar filtros, buscas e ordenações automaticamente

- Garantir segurança com autenticação e permissões

Tudo isso via interface web amigável, sem a necessidade de interagir diretamente com o banco de dados ou utilizar um SGBD como pgAdmin, DBeaver, etc.