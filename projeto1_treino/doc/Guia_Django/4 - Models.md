# Introdução 

ess documenta visa fazer uma breve explicação sobre o que seria Model da ORM específica do DJANGO

## Models

Models é uma forma que a ORM nativa do DJANGO fornece para podermos representar uma tabela do banco de dados, ou seja um entidade via programação POO (PROGRAMAÇÃO ORIENTADO A OBJETO), ou seja, criamos o nosso próprio modelo e esse modelo é criado dentro do banco de dados

## Relação de Model com Migretions

Todos os Model que definimos são criados e inseridos no banco de dados pela migrations sem termos que nos preocupar com scripts SQL

# Exemplo:

from django.db import models

# Crie os seus Models (Entidades do Banco de dados) aqui

    class Topic(models.Model): # fazendo uma herança 
        
        # definindo um atributo que será do tipo CharField com no máximo 200 caracteres, basicamente representa o nosso VARCHAR(200)
        text = models.CharField(max_length=200) 
        
        # # definindo um atributo da nossa classe que vai automaticamente adicionar data e hora do nosso computador neste campo
        date_added = models.DateTimeField(auto_now_add=True) 
        
        # crinado o nosso contrutor (opcional, não é obrigatório)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs) # atributo especial que chama o construtor da class pai
        
        '''
            Anotações sobre *args e **kwargs
            
            *args:
                
                É uma convenção, não uma palavra reservada do Python 
                (você poderia usar outro nome, mas é padrão usar args).

                O asterisco * significa: receber um número variável de argumentos 
                posicionais como uma tupla.

            **kwargs:
                
                Também uma convenção (significa “keyword arguments”).

                O ** significa: receber um número variável de argumentos nomeados 
                (chave=valor) como um dicionário.
        
        '''
        
        # criando um método para organizar o nosso administrativo. 
        def __str__(self):
            """ Devolve uma representação em string do Modelo. """
            return self.text # funciona como um this do java, basicamente vamos referenciar ao proprio atributo text