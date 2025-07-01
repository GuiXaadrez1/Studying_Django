# Principais atributos comuns nos campos de Models do Django

| Atributo         | Descrição                                                                 |
|------------------|---------------------------------------------------------------------------|
| `null`           | Permite armazenar `NULL` no banco de dados (padrão: `False`)             |
| `blank`          | Permite campo vazio nos formulários (validação em nível de formulário)    |
| `default`        | Define um valor padrão se nenhum for fornecido                            |
| `primary_key`    | Define o campo como chave primária do model                               |
| `unique`         | Garante que o valor seja único no banco de dados                          |
| `db_index`       | Cria um índice no campo (melhora performance de consulta)                 |
| `editable`       | Define se o campo aparece em formulários de admin ou model forms          |
| `choices`        | Define um conjunto de valores válidos (como ENUM)                         |
| `verbose_name`   | Nome legível usado na interface administrativa e documentação             |
| `help_text`      | Texto auxiliar exibido nos formulários/admin                              |
| `auto_now`       | Atualiza o campo com a data/hora atual **toda vez** que salvar            |
| `auto_now_add`   | Define a data/hora **apenas na criação** do registro                      |
| `validators`     | Lista de funções de validação personalizadas                              |
| `max_length`     | Tamanho máximo de caracteres (obrigatório em `CharField` e `EmailField`)  |
| `upload_to`      | Define o caminho de upload para arquivos/imagens (`FileField`, `ImageField`) |
| `on_delete`      | Define o comportamento ao deletar registros relacionados (`ForeignKey`)   |
| `related_name`   | Nome usado para acessar o relacionamento reverso em relações (`FK`, `ManyToMany`) |
| `to_field`       | Define qual campo da model relacionada será usado como chave estrangeira  |


## Campos (`Field`) do Django Models com descrição e exemplos

| Campo (`models.`)       | Descrição                                                                 | Exemplo com atributos                                                   |
|-------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `CharField`             | Texto de tamanho fixo (como `VARCHAR`)                                    | `models.CharField(max_length=100, blank=True)`                         |
| `TextField`             | Texto longo (`TEXT` no banco)                                              | `models.TextField(null=True)`                                          |
| `IntegerField`          | Número inteiro (`INT`)                                                     | `models.IntegerField(default=0)`                                       |
| `BigIntegerField`       | Número inteiro longo (`BIGINT`)                                            | `models.BigIntegerField()`                                             |
| `PositiveIntegerField`  | Inteiro positivo                                                           | `models.PositiveIntegerField()`                                        |
| `FloatField`            | Número com ponto flutuante (`FLOAT`)                                      | `models.FloatField()`                                                  |
| `DecimalField`          | Número decimal fixo (precisão alta, como `NUMERIC`)                        | `models.DecimalField(max_digits=5, decimal_places=2)`                  |
| `BooleanField`          | Campo booleano (`True` / `False`)                                          | `models.BooleanField(default=False)`                                   |
| `NullBooleanField`      | Booleano que aceita `NULL` (⚠️ obsoleto, use `BooleanField(null=True)`)     | `models.BooleanField(null=True)`                                       |
| `DateField`             | Apenas data (`YYYY-MM-DD`)                                                 | `models.DateField(auto_now_add=True)`                                  |
| `TimeField`             | Apenas hora (`HH:MM:SS`)                                                   | `models.TimeField(auto_now=True)`                                      |
| `DateTimeField`         | Data e hora                                                                | `models.DateTimeField(auto_now_add=True)`                              |
| `DurationField`         | Armazena diferença de tempo (ex: timedelta)                                | `models.DurationField()`                                               |
| `EmailField`            | Validação para e-mails                                                     | `models.EmailField(max_length=254)`                                    |
| `URLField`              | Validação para URLs                                                        | `models.URLField()`                                                    |
| `SlugField`             | Texto curto e único para URLs (sem espaços, acentos, etc.)                 | `models.SlugField(unique=True)`                                        |
| `UUIDField`             | Campo para UUIDs (identificadores únicos universais)                       | `models.UUIDField(default=uuid.uuid4, editable=False)`                 |
| `FileField`             | Para upload de arquivos                                                    | `models.FileField(upload_to='uploads/')`                               |
| `ImageField`            | Upload de imagem (herda de `FileField`)                                    | `models.ImageField(upload_to='img/')`                                  |
| `ForeignKey`            | Relacionamento muitos-para-um (chave estrangeira)                          | `models.ForeignKey(OutroModel, on_delete=models.CASCADE)`              |
| `OneToOneField`         | Relacionamento um-para-um                                                  | `models.OneToOneField(User, on_delete=models.CASCADE)`                 |
| `ManyToManyField`       | Relacionamento muitos-para-muitos                                          | `models.ManyToManyField(Grupo)`                                        |
| `JSONField`             | Armazena dados estruturados em JSON (desde Django 3.1 para todos os bancos)| `models.JSONField(default=dict)`                                       |
| `AutoField`             | Campo auto-incremental (ID padrão do Django)                               | `models.AutoField(primary_key=True)`                                   |
| `SmallIntegerField`     | Inteiros menores (`SMALLINT`)                                              | `models.SmallIntegerField()`                                           |
| `PositiveSmallIntegerField` | Inteiros positivos menores                                           | `models.PositiveSmallIntegerField()`                                   |

# Métodos comuns de Models no Django

| Método         | Descrição                                                                 | Exemplo com atributos usados                                  |
|----------------|---------------------------------------------------------------------------|----------------------------------------------------------------|
| `save()`       | Salva o objeto no banco de dados (insert/update).                        | `obj.save()` grava um novo ou atualiza um existente            |
| `delete()`     | Deleta o objeto do banco de dados (delete físico).                       | `obj.delete()` remove o registro permanentemente               |
| `__str__()`    | Retorna uma representação em string do objeto.                           | `def __str__(self): return self.nome`                          |
| `get_absolute_url()` | Retorna a URL absoluta para o objeto (usado com `reverse()`).     | `return reverse('detalhe_tarefa', args=[str(self.id)])`        |
| `clean()`      | Adiciona validações personalizadas no model (nível de model).            | `def clean(self): if self.preco < 0: raise ValidationError(...)` |
| `full_clean()` | Executa todas as validações (`clean_fields`, `clean`, `validate_unique`).| `obj.full_clean()`                                             |
| `save_model()` | Override usado no admin para lógica customizada ao salvar.               | `def save_model(self, request, obj, form, change): ...`        |
| `get_queryset()` | Usado em Managers e Views para customizar o conjunto de objetos.      | `def get_queryset(self): return super().get_queryset().filter(ativo=True)` |
| `create()`     | Cria e salva um novo objeto diretamente via Manager.                    | `Model.objects.create(nome="Exemplo", ativo=True)`             |
| `update()`     | Atualiza um ou mais objetos diretamente via `QuerySet`.                 | `Model.objects.filter(id=1).update(nome="Novo Nome")`          |
| `objects.filter()` | Retorna um queryset filtrado.                                       | `Model.objects.filter(ativo=True)`                             |
| `objects.get()`    | Retorna um único objeto que casa com o filtro (ou erro).           | `Model.objects.get(id=1)`                                      |
| `objects.all()`    | Retorna todos os registros da tabela.                              | `Model.objects.all()`                                          |
| `objects.exclude()`| Retorna todos **exceto** os que casam com o filtro.                | `Model.objects.exclude(status="inativo")`                      |
