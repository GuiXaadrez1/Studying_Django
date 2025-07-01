# Para que serve o self?

O self em Python é uma referência à instância atual da classe — ou seja, ele representa o objeto em si. Ele é obrigatório como primeiro parâmetro de qualquer método de instância, como __init__, __str__, ou métodos definidos por você.

## Analogia com o Java

Se você vem do Java, self é equivalente ao this. Ambos servem para acessar:

os atributos do próprio objeto,

outros métodos da mesma instância

## Exemplo prático:

class Pessoa:

    # construtor que exije um nome
    def __init__(self, nome):
        self.nome = nome  # 'self.nome' é o atributo do objeto; 'nome' é o parâmetro recebido

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}"

Uso:

    p = Pessoa("Guilherme")
    print(p.saudacao())  # Olá, meu nome é Guilherme

O que acontece aqui:

    self.nome = nome → o valor passado como argumento ("Guilherme") é armazenado dentro do objeto (self).

    self.nome é como dizer: “pegue o atributo nome desta instância atual”.

Por que é necessário?

Sem self, o Python não saberia de qual objeto estamos falando ao acessar atributos ou métodos. O self dá contexto ao método — “estou falando comigo mesmo”.