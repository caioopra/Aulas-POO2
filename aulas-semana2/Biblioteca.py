class Livro:
    def __init__(self, titulo, autores, ano, editora, edicao, volume):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume

    def getLivro(self):
        return [self.__titulo, self.__autores, self.__ano, self.__editora, self.__edicao, self.__volume]

    def __str__(self):
        return f"{self.__titulo}, {self.__autores} - {self.__ano}, {self.__editora}, edição {self.__edicao}, volume {self.__volume}"


# classe biblioteca possui lista com objetos do tipo Livro
class Biblioteca:
    def __init__(self, livros):
        self.__livros = livros

    def adicionarLivro(self, livro):
        self.__livros.append(livro)

    def consultarBiblioteca(self):
        return self.__livros

    def pesquisar(self, *atributos):
        livros = self.consultarBiblioteca()

        qtd_atributos = len(atributos)
        livros_iguais = []
        atributos_correspondentes = 0

        for livro in livros:
            atributos_livro = livro.getLivro()

            if all(atributo in atributos_livro for atributo in atributos):
                livros_iguais.append(livro)
                atributos_correspondentes += 1

        if atributos_correspondentes != qtd_atributos:
            print("Livro não encontrado, opções semelhantes: ")
        else:
            print("Livro encontrado: ")
            
        for livro_encontrado in livros_iguais:
            print(livro_encontrado)


livros = [Livro("Clean Code", "Robert C. Martin", 2009, "Editora 1", 3, 5),
          Livro("Livro2", "Autor Legal", 2020, "Editora 2", 2, 4), 
          Livro("Livro3", "Autor Legal", 2020, "Editora 3", 2, 4)]
biblioteca = Biblioteca(livros)

biblioteca.pesquisar("Autor Legal")
biblioteca.pesquisar("Clean Code")
