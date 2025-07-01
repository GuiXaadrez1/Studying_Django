1. o método def __str__(self):

em um modelo Django é usado para definir a representação textual (string) do objeto, ou seja, como ele vai aparecer quando você fizer:

print(objeto)

Visualizar objetos no admin do Django

Mostrar objetos em qualquer contexto que exija uma string

Exemplo:

    def __str__(self):
        """Devolve uma representação em string do Modelo."""
        return self.text

Retorna o valor do atributo text do objeto.

Ou seja, ao imprimir o objeto, será mostrado o conteúdo do campo text.


Por que isso é importante?

Sem o __str__, ao imprimir um objeto Django, você verá algo genérico como:

<MeuModelo: MeuModelo object (1)>

Com o __str__ implementado, você verá algo mais legível, útil para debug e interface:

<MeuModelo: Texto do campo text>

Equivalente ao toString() em Java:

Exatamente como você mencionou, é como o método toString() do Java, que define a forma como o objeto se representa como texto.