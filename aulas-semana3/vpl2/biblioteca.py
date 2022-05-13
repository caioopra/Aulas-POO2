from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if type(livro) != Livro:
            print("Livro inválido!")
        else:
            if livro in self.__livros:
                print("Livro já adicionado")
            else:
                self.__livros.append(livro)

    def excluirLivro(self, livro: Livro):
        if type(livro) != Livro:
            print("Livro inválido!")
        elif livro not in self.__livros:
            print("Livro não consta na biblioteca")
        else:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
