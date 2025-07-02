from django.shortcuts import render

# Crie a sua view aqui

def index(request):
    """Página principal do lerning_log"""
    return render(request, 'lerning_logs/index.html')

# a função render vai renderizar uma página html para o navegador do usuário