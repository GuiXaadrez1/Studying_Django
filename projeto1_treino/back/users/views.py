from django.http import HttpRequest,HttpResponse,HttpResponseRedirect # Classe de métodos http nativo do Django
from django.contrib.auth import login # método nativo que permite o login após uma autentificação
from django.contrib.auth import logout# método nativo do Django que realizar o logout
from django.contrib.auth import authenticate # método nativo do Django que autentifica credenciais do usuário
from django.contrib.auth.forms import UserCreationForm # Classe que cria um formulário para a criação de usuários
from django.shortcuts import render # método nativo do Django que renderiza o template no navegador do cliente
from django.urls import reverse # método nativo que redireciona para uma url específica


# nossa função que materializa o método logout para desligar sessão do usuário
def logout_view(request:HttpRequest)->HttpResponseRedirect:
    """ Faz o logout do Usuário """
    logout(request)
    return  HttpResponseRedirect(reverse('login')) 

# criando views para uma tela chamada de cadastro de usuário
def cadastro_user(request:HttpRequest)->HttpResponse:
    """ Faz o cadastro de um novo usuário """
    
    if request.method != 'POST':
        # se o método for diferente de POST, criar um formulário em Branco
        form = UserCreationForm()
    
    else:
        form = UserCreationForm(data=request.POST) # estamos passando dentro do parâmetro data a os dados preenchidos na requisição POST 
           
        if form.is_valid(): # validando os dados do formulário
            
            new_user = form.save() # salvando os dados no banco de dados
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
    
            # fazendo login
            if authenticate_user is not None:
                login(request, authenticate_user)
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, "Erro ao autenticar usuário após o cadastro.")
          
    # no final da função, o contexto e o rener deve ser no final da nossa estrutura de tomada de decisão
    context = {'form':form}
    return render(request,'users/cadastro_user.html',context=context,content_type='text/html',status=200)
    