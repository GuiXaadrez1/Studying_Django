# Introdução

Essa documentação visa explicar como funciona o formulário com DJANGO

##  que são formulários no Django?

Formulários no Django são classes que definem a estrutura de dados que o usuário pode enviar pela interface web. Eles são usados tanto para criação de dados quanto para validação de entrada antes que esses dados sejam salvos no banco de dados.

Existem dois principais tipos de formulários no Django:

    forms.Form: formulário comum, sem vínculo direto com um modelo

    forms.ModelForm: formulário baseado em um model, usado para criar ou editar instâncias do banco de dados


## Vamos criar um script.py padrão com python

Dentro do seu projeto de aplicação, você vai criar um script chava chamado de forms.py para o Django reconhecer o nosso formulário

## Por que usar formulários no Django?

    Validação automática dos dados

    Integração com os modelos (ORM)

    Geração automática de campos HTML com base no modelo

    Segurança contra ataques como CSRF

    Organização do código e separação de responsabilidades


## Exemplo de um ModelForm simples

- Dentro de forms.py:

    from django import forms
    from .models import Sala

    class SalaForm(forms.ModelForm):
        class Meta:
            model = Sala
            fields = ['nome', 'capacidade', 'descricao']


- Criando uma views para o formulário:

    from django.db import models

    class Sala(models.Model):
        nome = models.CharField(max_length=100)
        capacidade = models.IntegerField()
        descricao = models.TextField(blank=True)

        def __str__(self):
            return self.nome

- Criando uma template para o formulário:

    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Cadastrar Sala</title>
    </head>
    <body>
        <h1>Cadastro de Sala</h1>

        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Salvar</button>
        </form>

    </body>
    </html>


## PARÂMETROS PASSADOS PARA UMA INSTÂNCIA DO NOSSO FORMULÁRIO CRIADO EM FORMS.PY INICIALIZADO NO VIEWS.PY

| Parâmetro         | Tipo de Requisição | Descrição                                                                 |
|-------------------|--------------------|---------------------------------------------------------------------------|
| `data`            | `request.POST`     | Dados enviados pelo usuário em um formulário via POST (formulário preenchido). |
| `files`           | `request.FILES`    | Arquivos enviados pelo usuário via formulário (ex: imagens, PDFs).       |
| `instance`        | `Model instance`   | Instância de um model usada para editar dados existentes.                |
| `initial`         | `dict`             | Dicionário com valores iniciais dos campos do formulário.                |
| `prefix`          | `str`              | Prefixo usado para identificar os campos do formulário em páginas com múltiplos formulários. |
| `label_suffix`    | `str`              | Sufixo que aparece após os rótulos dos campos (ex: “:”).                 |
| `empty_permitted` | `bool`             | Se `True`, permite que o formulário seja enviado com campos vazios.     |
| `auto_id`         | `bool` ou `str`    | Define como os IDs dos campos são gerados (`True` usa padrão, `False` desativa). |


## EXEMPLOS PRÁTICOS


- Exemplo de criação (formulário vazio):

form = SalaForm()

- Exemplo de criação com dados POST:

    form = SalaForm(request.POST)

- Exemplo de edição de objeto existente:
    
    sala = Sala.objects.get(id=1)
    form = SalaForm(instance=sala)

Exemplo com valores iniciais:

- form = SalaForm(initial={'nome': 'Sala A', 'capacidade': 50})

- Exemplo com arquivos:

    form = SalaForm(request.POST, request.FILES)