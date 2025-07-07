# Arquivo responsável por criar o nosso formulário
from django import forms
from .models import Topic, Entry


# Vamos criar classe referente aos nossos formulários 
# Que vai herder do django todos os atributos da entidade forms.ModelForm

class TopicForm(forms.ModelForm): # lembre-se anotação de  retorno não funciona para classes em python, somente em métodos ou funções
    
    # class meta
    class Meta():
        model = Topic  # Modelo vinculado ao formulário
        fields = ['text']  # Campos do modelo que serão exibidos no formulário
        labels = {'text': ''}  # Rótulo personalizado para o campo "text"
        
class EntryForm(forms.ModelForm):
    
    class Meta():
        model = Entry
        fields = ['annotations']
        labels = {'annotations':''}
        widgets = {'annotations':forms.Textarea(attrs={'cols':80})} # define o tipo de input HTML de cada campo