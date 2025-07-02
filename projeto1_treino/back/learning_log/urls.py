"""
Configuração de URLs para o projeto learning_log.

A lista `urlpatterns` direciona URLs para as views. Para mais informações, veja:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Exemplos:

Views baseadas em função:
    1. Adicione uma importação:  from my_app import views
    2. Adicione uma URL à lista urlpatterns:  path('', views.home, name='home')

Views baseadas em classe:
    1. Adicione uma importação:  from other_app.views import Home
    2. Adicione uma URL à lista urlpatterns:  path('', Home.as_view(), name='home')

Incluindo outra configuração de URLs:
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL à lista urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('lerning_logs.urls')) 
]
