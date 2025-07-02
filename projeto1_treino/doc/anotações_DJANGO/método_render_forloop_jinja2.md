# Relacionamento entre Models e Banco de Dados no Django

Os models são as representações das nossas entidades no banco de dados.
Com base nisso, fazemos a ligação com o banco, pois ele está diretamente relacionado ao model.

## render() no Django

A função render() é usada para gerar uma resposta HTTP que contém o HTML renderizado com dados dinâmicos.

| Parâmetro       | Tipo             | Obrigatório | Descrição                                                            |
| --------------- | ---------------- | ----------- | -------------------------------------------------------------------- |
| `request`       | `HttpRequest`    | ✅ Sim       | Objeto de requisição HTTP recebido do navegador                      |
| `template_name` | `str`            | ✅ Sim       | Caminho do arquivo de template HTML dentro da pasta `templates/`     |
| `context`       | `dict` ou `None` | ❌ Não       | Dicionário com dados para passar ao template (`{{ var }}` no HTML)   |
| `content_type`  | `str` ou `None`  | ❌ Não       | Tipo de conteúdo da resposta (`text/html`, `application/json`, etc.) |
| `status`        | `int` ou `None`  | ❌ Não       | Código de status HTTP da resposta (ex: 200, 404, 403)                |
| `using`         | `str` ou `None`  | ❌ Não       | Nome do backend de template se estiver usando múltiplos (raro)       |

## Exemplo prático


Front-end:

{% for topico in topicos %}
    <p>{{ topico.text }}</p>
{% endfor %}


## render(request, 'pasta/template.html', {'variavel_template': valor_backend})

Leva dados do back-end → para o front-end

Encapsula os dados no HTML gerado pelo template

Retorna uma resposta HTTP renderizada

## Exemplo com todos os parâmetros:

from django.shortcuts import render

def minha_view(request):
    dados = {'nome': 'Guilherme'}
    return render(
        request,                      # requisição recebida
        'meu_app/pagina.html',       # caminho do template
        context=dados,               # contexto com dados para o template
        content_type='text/html',    # tipo de conteúdo da resposta
        status=200,                  # código de status HTTP
        using=None                   # backend de template (raro uso)
    )

# Estrutura de repetição com Jinja2 (usada no Django Templates)

1. A view retorna a variável topics com um queryset:

    topics = Topic.objects.order_by('date_added')

2. No template:

    {% for topic in topics %}
        <p>{{ topic.text }}</p>
    {% empty %}
        <p>Nenhum tópico encontrado.</p>
    {% endfor %}

3. A variável topic representa cada instância do model Topic.

4. O bloco {% empty %} é executado se topics estiver vazio.

5. Importante - Para {{ topic }} exibir corretamente, o model deve sobrescrever o método __str__:

def __str__(self):
    return self.text

# Especificando como uma função do Back-end pode retornar um template, html renderizado para o Front-end

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Topic

def topics(request: HttpRequest) -> HttpResponse:
    """Página que mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'lerning_logs/topics.html', context)
