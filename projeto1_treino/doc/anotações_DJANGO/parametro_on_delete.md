# parametro on_delete ORM nativa do DJANGO

esse parametro na ORM é utilizado quando estamos definido um FK no MODELS e como queremos 
definir o comportamento do DELETE para a entidade filha (quem ela referencia/dependente)
e entidade pai (referenciado).

É um parametro obrigatório e possui várias opções, que vêm do módulo django.db.models

OBS_IMPORTANTE: TODAS AS OPÇÕES ABAIXO É PARA DELETE FÍSICO NO BANCO DE DADOS E NÃO LÓGICO

class Entry(models.Model):

    # criando atributos, lembre-se que é opcional criar um construtor
    
    topic = models.ForeignKey(Topic, on_delete = SET_NULL ) 


# OPÇÕES DISPONÍVEIS PARA SER USADAS:

1. CASCADE

Deleta automaticamente o objeto relacionado (filho) se o pai for deletado.

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

🔥 Muito usado. Ex: deletar um tópico apaga todos os itens relacionados a ele.

2. PROTECT

Impede que o objeto pai seja deletado se houver filhos relacionados.

    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)

🔐 Garante integridade: lança ProtectedError se tentar deletar o pai.

3. SET_NULL

Define o campo como NULL se o objeto pai for deletado.

    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)

🟡 Requer null=True.

Útil quando o relacionamento é opcional.

4. SET_DEFAULT

Atribui um valor padrão ao campo se o pai for deletado.

    topic = models.ForeignKey(Topic, default=1, on_delete=models.SET_DEFAULT)

🧩 Requer que default esteja definido no campo.

5. SET(...)
Executa uma função ou atribui um valor específico.

    topic = models.ForeignKey(Topic, on_delete=models.SET(lambda: get_default_topic()))
    
    ou

    topic = models.ForeignKey(Topic, on_delete=models.SET(1))  # Define ID fixo

🧠 Usado para lógica personalizada.

6. DO_NOTHING
Não faz nada — o banco pode lançar erro de integridade.

    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)

⚠️ Perigoso. Deixa a integridade referencial por sua conta (usado quando o banco tem triggers ou constraints manuais).

7. RESTRICT (desde Django 3.1+)

Impede a deleção se houver referência, mas sem lançar ProtectedError.

    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT)

🔍 Semelhante ao PROTECT, mas mais suave e sem exceptions do tipo ProtectedError.


# TABELA COMPARATIVA

## Opções para `on_delete` no Django

| Opção             | Comportamento ao deletar o objeto pai         | Requisitos / Observações                            |
|------------------|------------------------------------------------|-----------------------------------------------------|
| `models.CASCADE`   | Deleta automaticamente o objeto filho         | Muito usado; uso comum em relacionamentos fortes    |
| `models.PROTECT`   | Impede a deleção do pai se houver dependentes | Lança `ProtectedError`                              |
| `models.SET_NULL`  | Define o campo como `NULL`                    | Requer `null=True` no campo                         |
| `models.SET_DEFAULT` | Define o valor padrão do campo              | Requer `default=...` no campo                       |
| `models.SET(...)`  | Atribui um valor fixo ou executa uma função  | Ideal para lógica personalizada                     |
| `models.DO_NOTHING`| Nenhuma ação; deixa integridade ao banco      | Pode causar erro de integridade referencial ⚠️      |
| `models.RESTRICT`  | Impede a deleção se houver referência         | Disponível a partir do Django 3.1                   |
