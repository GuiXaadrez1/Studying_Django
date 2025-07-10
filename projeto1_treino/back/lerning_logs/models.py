from django.db import models
from django.contrib.auth.models import User # importando Class usuário, nativa do próprio Django

# Crie os seus Models (Entidades do Banco de dados) aqui

class Topic(models.Model): # fazendo uma herança 
    
    # definindo um atributo que será do tipo CharField com no máximo 200 caracteres, basicamente representa o nosso VARCHAR(200)
    text = models.CharField(max_length=200) 
    
    # definindo um atributo da nossa classe que vai automaticamente adicionar data e hora do nosso computador neste campo
    date_added = models.DateTimeField(auto_now_add=True)
    
    # vinculando um dono a um tópico em específico
    owner =  models.ForeignKey(User, on_delete=models.CASCADE) # Materializando o nosso usuário nativo como uma FK
    
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
    
    
class Entry(models.Model):

    # criando atributos, lembre-se que é opcional criar um construtor
    
    # puxando a FOREIGN KEY da ENTIDADE TOPIC, ligação entre ENTRY E TOPIC
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) # Entry vai ser deletado junto com o atributo pai
    annotations = models.TextField() # valor ilimitado de caracteres
    date_added = models.DateTimeField(auto_now_add=True)

    # opcional colcoar, porém interessante para corrigir algum bug com Entry no fututo
    class Meta(): 
        verbose_name_plural = 'entries'
    
    def __str__(self):
       return f"[{self.topic}] {self.annotations[:50]}..." # retornando os primeiro 50 caracteres + ...
    
    