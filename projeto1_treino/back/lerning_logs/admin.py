from django.contrib import admin
from lerning_logs.models import Topic # importando da pasta da nossa aplicação do arquivo models a Class Topic
from lerning_logs.models import Entry

# Registre o seu Model aqui
admin.site.register(Topic) # Registrando a nossa Class Topic
admin.site.register(Entry) # Registrando a Class Entry

