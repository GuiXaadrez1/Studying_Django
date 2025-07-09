from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.contrib.auth import login # método nativo que permite o login após uma autentificação
from django.contrib.auth import logout# método nativo do Django que realizar o logout
from django.shortcuts import render
from django.urls import reverse


# nossa função que materializa o método logout para desligar sessão do usuário
def logout_view(request:HttpRequest)->HttpResponseRedirect:
    """ Faz o logout do Usuário """
    logout(request)
    return  HttpResponseRedirect(reverse('login')) 

# criando views para uma tela chamada de cadastro de usuário
