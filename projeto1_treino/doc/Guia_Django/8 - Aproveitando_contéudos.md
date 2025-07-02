# INTRODUÇÃO

essa documentação visa fazer um guia rápido para aproveitarmos contéudos, componentes de outras páginas:

- Para fazermos isso, vamos criar uma página que tempos componetes em comum e posteriormente ao contruir outra páginas que precisam destes componete, essas páginas construidas irão herder a os componentes da página pai... Herança de páginas, funciona como se fosse o conceito de herança em programação orientado a objeto.

dentro da subpasta lerning_log na pasta Templates, vamos criar um html chamado de base.html (nossa página pai)


# JINJA2

O DJANGO tem suporte com a linguagem de templates para dinâmismo de página chamado de JINJA2, clique neste link: https://jinja.palletsprojects.com/en/stable/ para mais informações a respeito do JINJA2, porém saiba que o DJANGO tem uma estrutura próprio para o sistema de templates

## Estrutura esperada para herança de templates

meuprojeto/
├── templates/
│   └── lernin_logs/
│       ├── base.html      <- template base (estrutura do site)
│       └── index.html     <- template filho (página inicial)

##  Como o base.html funciona
Ele é o template-pai, onde você define a estrutura comum do site:
    <!-- templates/lernin_logs/base.html -->
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}Título padrão{% endblock title %}</title>
    </head>
    <body>
        <header>
            <h1>Minha Aplicação Django</h1>
            <nav><a href="{% url 'index' %}">Início</a></nav>
        </header>

        <main>
            {% block content %}
            <!-- Aqui o conteúdo das páginas será inserido -->
            {% endblock content %}
        </main>

        <footer>
            <p>Rodapé fixo</p>
        </footer>
    </body>
    </html>

- Esse arquivo não será renderizado diretamente. Ele só serve de base para os outros.

##  Como o index.html herda do base.html

O index.html é um template-filho que herda do base.html com a diretiva {% extends %} e preenche os blocos definidos lá (title e content):

    <!-- templates/lernin_logs/index.html -->
    {% extends "lerning_logs/base.html" %}

    {% block title %}Página Inicial{% endblock title %}

    {% block content %}
        <p>Essa aplicação ajudará a entender como funciona o roteamento de rotas com Django.</p>
    {% endblock content %}

Note que não existe nenhum <html>, <head> ou <body> aqui — tudo isso já está no base.html. O index.html só define o que vai dentro dos blocos.

## Explicação rápida sobre: {% block nome %} ... {% endblock %}  e {% extends "base.html" %} 

1. {% block nome %} ... {% endblock %} 

Significado: Define regiões substituíveis dentro do template pai (base).

Exemplo:

    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}Título Padrão{% endblock title %}</title>
    </head>
    <body>
        {% block content %}
        <!-- Conteúdo padrão -->
        {% endblock content %}
    </body>
    </html>

2. {% extends "base.html" %} 

Significado: A diretiva {% extends %} indica que o template atual herda de outro.

Onde usar: Sempre como a primeira linha do arquivo de template. Antes mesmo de <!DOCTYPE html>.

Exemplo:

    {% extends "lerning_logs/base.html" %}

    {% block title %}Página Inicial{% endblock title %}

    {% block content %}
        <h1>Bem-vindo!</h1>
        <p>Esta é a página principal do projeto Django.</p>
    {% endblock content %}
