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
