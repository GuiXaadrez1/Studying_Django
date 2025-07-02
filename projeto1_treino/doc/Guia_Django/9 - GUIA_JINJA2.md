# INTRODUÇÃO
Esse documento tem como objetivo ser um guia para entendermos sobre a linguagem de templates JINJA2.

## O que é Jinja2?

Jinja2 é um mecanismo de templates moderno, rápido e seguro para Python, usado para gerar HTML dinamicamente. É amplamente utilizado em frameworks como Flask e inspirou a sintaxe do Django Template Language.

- Características:

    Sintaxe semelhante ao Python

    Suporte a expressões, filtros, loops, macros e herança

    Separação clara entre lógica e apresentação (MVC/MVT)

## SINTAXE BÁSICA:

1. Declaração, manipulação apresentação de variáveis no template:

    Sintaxe: {{ variavel }}

As chaves {{ }} indicam que estamos imprimindo o valor da variável na página HTML.

As variáveis não são "declaradas" no Jinja2 como em linguagens como Python ou JavaScript; elas são passadas para o template pelo código do servidor.

Exemplo:

    {{ nome }}  # variável simples 
    {{ usuario.email }} # acessando propriedades de objetos
    {{ produto['preco'] }} # acessando valores de dicionários 

- Variáveil simples: 

    Se o backend passou nome = "Guilherme", o template imprimirá Guilherme.

- Acessando propriedades de objetos: 

    Isso acessa o atributo email do objeto usuario.

    Exemplo: Se no Python você tem usuario = Usuario(email="exemplo@email.com"), o Jinja imprime exemplo@email.com.

- Acessando valores de dicionários:

    Acessa o valor com chave 'preco' do dicionário produto.

    Exemplo: Se produto = {"nome": "Camisa", "preco": 59.90}, a saída será 59.90.

- Regras importantes:

    É possível acessar:

        atributos de objetos (como .nome)

        índices de listas (lista[0])

        chaves de dicionário (dado['chave'])

    Não é possível:

        Declarar variáveis diretamente como em Python: nome = "Guilherme" não funciona dentro de {{ }}.

        Fazer atribuições com = dentro de {{ }}. Isso é feito com {% set %} (veremos adiante).

2. Atribuindo variáveis dentro do template:

    {% set total = 10 + 20 %}
    Total: {{ total }}

set permite criar e atribuir valores a variáveis dentro do template.

Ideal para operações simples, soma de valores, contadores, etc.

Exemplo Completo:

    <!DOCTYPE html>
    <html>
    <body>
        <h1>Olá, {{ usuario.nome }}!</h1>
        <p>Email: {{ usuario.email }}</p>
        <p>Produto: {{ produto['nome'] }} - R$ {{ produto['preco'] }}</p>

        {% set desconto = produto['preco'] * 0.1 %}
        <p>Desconto (10%): R$ {{ desconto }}</p>
    </body>
    </html>

- Boa Práticas

    Sempre verifique se a variável existe antes de acessá-la. Você pode usar filtros:

    {{ produto['preco'] | default("Indisponível") }}

    Use set com moderação — evite lógica complexa nos templates.

3. Colocando comentários

{# Isso é um comentário #}

Bem auto-explicativo, não vai impactar o nosso template, básicamente é um <!---->, porém, uma observação: 

    NÃO MISTURE COMENTÁRIO HTML COM LINGUAGEM DE TEMPLATE, O DJANGO NÃO CONSEGUE RECONHECER A DIFERENÇA, EXEMPLO:

    <!--

        isso é um comentário que o DJANGO VAI RECLAMAR POSTERIORMENTE
        {% block content %}
            ...
        {% endblock content %}  
    -->

4. Operadores aritméticos 

Você pode usar os mesmos operadores do Python diretamente dentro das chaves {{ }}:

    {{ idade + 10 }}

Significado: Soma 10 ao valor da variável idade.

Se idade = 20, a saída será 30.

Outros operadores aritméticos:

| Expressão          | Descrição                 | Resultado (exemplo)    |
| ------------------ | ------------------------- | ---------------------- |
| `{{ idade + 10 }}` | Soma                      | `30` (se `idade = 20`) |
| `{{ 10 - 3 }}`     | Subtração                 | `7`                    |
| `{{ 4 * 2 }}`      | Multiplicação             | `8`                    |
| `{{ 20 / 4 }}`     | Divisão                   | `5.0`                  |
| `{{ 20 // 6 }}`    | Divisão inteira           | `3`                    |
| `{{ 9 % 4 }}`      | Módulo (resto da divisão) | `1`                    |

5. Operadores de Comparação

Servem para verificar condições dentro de estruturas de controle (if, for, etc).

| Expressão                  | Significado    |
| -------------------------- | -------------- |
| `{% if idade == 18 %}`     | Igualdade      |
| `{% if nome != "admin" %}` | Diferença      |
| `{% if preco > 100 %}`     | Maior que      |
| `{% if idade < 18 %}`      | Menor que      |
| `{% if nota >= 7 %}`       | Maior ou igual |
| `{% if idade <= 17 %}`     | Menor ou igual |

6. Operadores Lógicos

| Operador | Exemplo                                 | Significado    |
| -------- | --------------------------------------- | -------------- |
| `and`    | `{% if idade > 18 and ativo %}`         | E lógico       |
| `or`     | `{% if user.is_admin or user.is_mod %}` | OU lógico      |
| `not`    | `{% if not ativo %}`                    | Negação lógica |


7. Filtros (pipes|)

Filtros são usados com | para transformar o valor de uma variável.

    {{ nome|upper }}

Se nome = "guilherme", o resultado será GUILHERME.

upper é um filtro que transforma o texto em maiúsculas.


| Filtro       | Exemplo    | Resultado              |                                  |
| ------------ | ---------- | ---------------------- | -------------------------------- |
| `upper`      | \`{{ nome  | upper }}\`             | "GUILHERME"                      |
| `lower`      | \`{{ nome  | lower }}\`             | "guilherme"                      |
| `title`      | \`{{ nome  | title }}\`             | "Guilherme Henrique"             |
| `capitalize` | \`{{ nome  | capitalize }}\`        | "Guilherme henrique"             |
| `length`     | \`{{ lista | length }}\`            | Quantidade de itens da lista     |
| `default`    | \`{{ idade | default(0) }}\`        | Valor padrão se `idade` for None |
| `replace`    | \`{{ nome  | replace("a", "4") }}\` | Substitui letras                 |
| `round`      | \`{{ media | round(2) }}\`          | Arredonda com 2 casas decimais   |
| `join`       | \`{{ lista | join(", ") }}\`        | Junta elementos com separador    |

8. Encadeando filtros

    {{ nome|replace("e", "3")|upper }}

Substitui "e" por "3" e depois converte para maiúsculas.

Ex: guilherme → guilh3rm3 → GUILH3RM3.


9. Exemplo_completo:

    {% set idade = 25 %}
    {% set nome = "guilherme henrique" %}
    <p>Idade atual: {{ idade }}</p>
    <p>Daqui a 10 anos: {{ idade + 10 }}</p>
    <p>Nome: {{ nome|title }}</p>
    <p>Nome em letras maiúsculas: {{ nome|upper }}</p>
    <p>Nome com 'e' substituído por '3': {{ nome|replace("e", "3") }}</p>

## Controle dde Fluxo

Basicamente é um if, elif e else do python, segue o exemplo:

{% if user.is_authenticated %}
    Olá, {{ user.username }}!
{% elif user.is_guest %}
    Visitante
{% else %}
    Acesso negado
{% endif %}

Fazer a estrutura de tomada de decisão/controle de fluxo vai depender da sua lógica de programação e de como você precisa resolver aquele problema.


## Loops

Basicamente é um forloop do python, segue o exemplo:

<ul>
{% for produto in produtos %}
    <li>{{ produto.nome }} - {{ produto.preco }}</li>
{% endfor %}
</ul>

variáveis específicas do forloop:

| Variável        | Significado                    |
| --------------- | ------------------------------ |
| `loop.index`    | Índice do item (começa em 1)   |
| `loop.index0`   | Índice do item (começa em 0)   |
| `loop.revindex` | Posição reversa (último é 1)   |
| `loop.first`    | Verdadeiro no primeiro item    |
| `loop.last`     | Verdadeiro no último item      |
| `loop.length`   | Tamanho total da lista iterada |


Fazer a estrutura de repetição vai depender da sua lógica de programação e de como você precisa resolver aquele problema.


## Controle de loop

FoorLoop + if,ifelse e else... Basicamente uma programação python dentro de templates com JINJA, muito similhar a linguagem python, segue o exemplo:

{% for item in lista %}
    {% if loop.first %}(Primeiro){% endif %}
    {% if loop.last %}(Último){% endif %}
    {{ loop.index }} - {{ item }}
{% endfor %}

Fazer essa operação lógica vai depender da sua lógica de programação e de como você precisa resolver aquele problema.

# Filtros 

Filtros transformam valores: {{ valor|filtro }}

| Filtro          | Efeito                         |
| --------------- | ------------------------------ |
| `upper`         | Transforma texto em maiúsculas |
| `lower`         | Transforma texto em minúsculas |
| `default('x')`  | Usa valor padrão se nulo       |
| `length`        | Conta quantos itens            |
| `date('d/m/Y')` | Formata data (em Flask)        |

Exmeplo:

{{ nome|upper }}
{{ produtos|length }}


## Herança de Templates

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


## Macros e Includes no JINJA2

### O que são Macros

Macros são como funções no template Jinja2. Permitem reutilizar blocos de HTML com parâmetros dinâmicos, evitando repetição de código.

### SINTAXE:

    {% macro nome_macro(param1, param2) %}
        ...código HTML...
    {% endmacro %}

Exemplo:

    {% macro mostrar_produto(nome, preco) %}
        <li>{{ nome }} - R$ {{ preco }}</li>
    {% endmacro %}

    <ul>
        {{ mostrar_produto("Camiseta", 59.90) }}
        {{ mostrar_produto("Calça", 99.90) }}
    </ul>

### O que são Includes
Includes servem para inserir o conteúdo de outro arquivo de template dentro do atual. Útil para cabeçalhos, rodapés, menus etc.

### SINTAXE

    {% include "caminho/arquivo.html" %}

EXEMPLO:
    <!-- base.html -->
    <html>
    <body>
        {% include "partials/navbar.html" %}
        <div class="conteudo">
            {% block conteudo %}{% endblock %}
        </div>
        {% include "partials/footer.html" %}
    </body>
    </html>

Exemplo prático com macro + include:

    <!-- arquivo: components/produto.html -->
    {% macro card(nome, preco) %}
    <div class="card">
    <h2>{{ nome }}</h2>
    <p>R$ {{ preco }}</p>
    </div>
    {% endmacro %}

        <!-- template principal -->
    {% import "components/produto.html" as produto %}
    {{ produto.card("Tênis", 199.90) }}

### Boas práticas

| Prática                                   | Explicação                                     |
| ----------------------------------------- | ---------------------------------------------- |
| Use macros para componentes reutilizáveis | Cartões, botões, itens de lista, etc.          |
| Use includes para layout fixo             | Cabeçalho, rodapé, navbar, sidebar             |
| Separe arquivos por função                | `components/`, `partials/`, `layout/`          |
| Nomeie bem macros                         | `render_item`, `show_card`, `user_badge`, etc. |


## BOAS PRÁTICAS NA HORA DE CONSTRUIR TEMPLATES COM JINJA2

Mantenha lógica mínima nos templates

Use herança para evitar duplicação

Crie componentes reutilizáveis com include e macro

Evite acessar funções complexas dentro de {{ }}

Sempre escape inputs do usuário