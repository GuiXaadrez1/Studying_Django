# o que significa esse *args ou **kwargs?

1. *args:

É uma convenção, não uma palavra reservada do Python (você poderia usar outro nome, mas é padrão usar args).

O asterisco * significa: receber um número variável de argumentos posicionais como uma tupla.

Exemplo:

    def soma(*args):
        total = 0
        for n in args:
            total += n
        return total

    print(soma(1, 2, 3))  # Saída: 6
    print(soma(5, 10))    # Saída: 15

obs.: Aqui, *args permite passar qualquer quantidade de parâmetros posicionais para a função.


2. **kwargs

Também uma convenção (significa “keyword arguments”).

O ** significa: receber um número variável de argumentos nomeados (chave=valor) como um dicionário.

Exemplo:

    def imprime_info(**kwargs):
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")

    imprime_info(nome="João", idade=30)
    # Saída:
    # nome: João
    # idade: 30

obs.: Aqui, **kwargs permite passar qualquer quantidade de argumentos nomeados para a função.

# Por que usar em __init__ do Django?

No caso do Django, quando sobrescrevemos o __init__, usamos:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

Isso porque o construtor original do Django Model aceita muitos argumentos posicionais e nomeados, que são tratados internamente. Para não quebrar essa funcionalidade, você:

Recebe todos os argumentos que forem passados (mesmo que você não saiba quantos são).

Repassa para o construtor original com super().__init__(*args, **kwargs).

Assim, o funcionamento do Django Model permanece intacto.


# Criar um contrutor para classe definida no modelo é opcional porque:

O Django já implementa um construtor poderoso dentro de models.Model que sabe lidar com todos os campos que você definiu, além de parâmetros extras.

Quando você cria um modelo assim:

    class MeuModelo(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

Você já pode instanciar objetos passando os campos direto, sem precisar criar __init__:

    obj = MeuModelo(text="Olá Mundo!")
