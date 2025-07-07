# INTRODUÇÃO
Essa documentação tem como objetivo trazer soluções para resolver problemas de ambiente virtual .venv do python

## Ambiente virtual não está sendo reconhecido

Exemplo:

    PS C:\fabricadesoftware-salas\reserva_salas> python --version           
    Python 3.13.2
    PS C:\fabricadesoftware-salas\reserva_salas>  .\venv\Scripts\Activate.ps1
    .\venv\Scripts\Activate.ps1 : O termo '.\venv\Scripts\Activate.ps1' não é reconhecido como nome de cmdlet, função, arquivo de script ou programa operável. Verifique a grafia do nome ou, se um caminho tiver sido incluído, veja se o   
    caminho está correto e tente novamente.
    No linha:1 caractere:2
    +  .\venv\Scripts\Activate.ps1
    +  ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : ObjectNotFound: (.\venv\Scripts\Activate.ps1:String) [], CommandNotFoundException
        + FullyQualifiedErrorId : CommandNotFoundException


- Solução:

1. Verifique se a pasta venv existe

Execute no PowerShell:
    Get-ChildItem .\venv\Scripts\

Se você não ver arquivos como Activate.ps1, activate.bat, python.exe, então o ambiente virtual não foi criado corretamente.

2. Se não existir, crie o ambiente virtual

Execute:
    python -m venv venv

Isso criará a pasta venv/ com todos os scripts de ativação.

Depois, tente novamente ativar:
    
    .\.venv\Scripts\Activate.ps1

3. Se a pasta existir, mas ainda der erro, verifique a política de execução do PowerShell

- O PowerShell pode bloquear a execução de scripts por padrão.

Execute:

    Get-ExecutionPolicy

- Se o resultado for "Restricted", você pode permitir scripts temporariamente com:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Depois tente novamente:
    
    .\venv\Scripts\Activate.ps1


### explicão rápida do comando:

Explicação rápida:

    RemoteSigned: permite executar scripts locais sem assinatura.

    -Scope Process: aplica só para esta sessão do terminal (não afeta o sistema todo).

    Isso não representa risco de segurança, já que é temporário e controlado.


4. Como alternativa, use o CMD (Prompt de Comando)

    .\venv\Scripts\activate.bat


## Conclusão:

Seu erro provavelmente tem uma das seguintes causas:

    O ambiente virtual ainda não foi criado

    O PowerShell está bloqueando execução de scripts

    O caminho informado está errado ou incompleto



