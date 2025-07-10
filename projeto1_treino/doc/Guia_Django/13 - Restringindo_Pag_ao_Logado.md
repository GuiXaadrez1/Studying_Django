# INTRODUÇÃO
Esse documento tem como objetivo mostrar uma forma de restringir acesso de páginas somente a quem está logado

## Primeiro vamos definir deixar como constante o caminho da pagina login em settings.py na estrutura principal do nosso DJANGO

    # URL LOGIN PAGE, caminho para a nossa página de login
    LOGIN_URL = '/users/login'

## Segundo importar o decorador que se o usuário não estiver logado, vai ser redirecionado para a página login

    from django.contrib.auth.decorators import login_required

## Usar o decorador na função da view desejada

    @login_required # usando o nosso decorador
    def index(request:HttpRequest)->HttpResponse:
        """Página principal do lerning_log"""
        return render(request, 'lerning_logs/index.html') # a função render vai renderizar uma página html para o navegador do usuário
    