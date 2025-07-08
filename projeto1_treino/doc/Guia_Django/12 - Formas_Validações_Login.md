# INTRODUÇÃO

esse aquivo tem como objetivo mostrar formas diferentes de validar dados de um formulário de login

## Dentro do nosso arquivo urls.py no projeto aplicação users:

    from django.shortcuts import render
    import . import views

    urlspatters = [
        path('login',views.login, name = 'login') # forma tradicional
    ]


## Dentro do nosso template em users/login.html

    {% extends "lerning_logs/base.html" %}

    {% block content %}

        {% if form.errors %}
            <p>Seu login e senha estão incorretos! Por favor, tente novamente.</p>
        {% endif %}

        <form action="{% url 'login' %}" method="post">
            {% csrf_token %}
            {{form.as_p}}
            <button name = "submit">Entrar</button>
            <!-- caso os dados sejam validados, redirecionar para o index-->
            <input type="hidden" name="next" value="{% url 'index' %}">
            <!-- esse input é um input escondido, não atrapalha na visualização do nosso template -->
        </form>

    {%  endblock content %}


# CRIANDO O NOSSO PRÓPRIO FORMULÁRIO DE LOGIN SEM PRECISAR DO auth_views.LoginView.as_view(template_name='users/login.html')


1. primeiro form.py (usando o jango.contrib_auth.models ), de forma nativa

    from django.contrib_auth.models import User # estamos importando uma model de User que é o usuário nativo no nosso DJANGO
    from django import forms # importando módulo forms, basicamente criamos formulários html com ele

    class LoginForm(form.ModelForm): # criando classe que gera o nosso formulário
        class Meta(): # classe que configura como a classe LoginForm se comportará
            model = User
            fields = ['username','password']
            labels = {'username':'Login','password':'Senha'}


2. Outra forma de criar o fomrulário no DJANGO, usando o forms padrão do DJANGO



    from django import Forms # utilizar atributos e métodos nativos da Class Forms, basicamente é igual criar Models
    from django.core.exceptions import ValidationError

    -- Lembrando que existe diversas formas de personalizar validações no Django

    class LoginForm(forms.Form):
        login = forms.CharField(max_lenght = 30) # crinado os nossos campos de input 
        senha = forms.CharField(max_lenght = 30, widget = forms.PasswordInput()) # criando os nossos campos de input 

        def clean(): função que vamos usar para pegar dois campos ao mesmo tempo

                """
                    def clean(self):
                        cleaned_data = super().clean()
                        nome = cleaned_data.get('login')
                        senha = cleaned_data.get('senha')
                """

            nome = self.cleaned_data['login']

            if not(nome.isalnum()):
                raise ValidationError('O nome de usuário não pode ter caracter especial')
            
            returno nome


2. criar uma views

    from django.shortcuts import render
    from django.http import HttpRequest, HttpResponse, HttResponseRedirect
    from django.urls import reverse
    from .forms import LoginForm
    from django.contrib.auth import authenticate # método que verifica o username, email, senha ... e define se o usuário pode ser autentificado
    from djnago.contrib,auth import login as authLogin

    def login(request:HttpRequest)->HttpResponse:
        
        error = False

        if request.method != 'POST':
            form = LoginForm()
        else:
            form = LoginForm(data=request.POST)

            if form.is_valid(): # retorna um valor BOOLEANO, TRUE para valido e False para inválido
                username = request.POST.get('username') # puxando informações através de uma requisição http POST do campo password
                password = request.POST.get('password') # puxando informações através de uma requisição http POST do campo username
                user = authenticate(username = username, password = password) # verifica se pode ou não ser autentificado
                
                if user:
                    authLogin(request, user):
                    return HttpResponseRedirect(reverse('index'))
                else: 
                    error = True

        context = {'form':form, 'error':error}
        return render(request,'users/login.html', context, content_type = 'text/html')

3. Criando o nosso template

    {% extends "lerning_logs/base.html" %}

    {% block content %}

        {% if error  %}
            <p>Seu login e senha estão incorretos! Por favor, tente novamente.</p>
        {% endif %}

        <form action="{% url 'login' %}" method="post">
            {% csrf_token %}
            {{form.as_p}}
            <button name = "submit">Entrar</button>
            <!-- caso os dados sejam validados, redirecionar para o index-->
            <input type="hidden" name="next" value="{% url 'index' %}">
            <!-- esse input é um input escondido, não atrapalha na visualização do nosso template -->
        </form>

    {%  endblock content %}




