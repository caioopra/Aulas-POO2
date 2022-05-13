from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora,
                 autores: Autor = "", numeroCapitulo: int = 0, tituloCapitulo: str = ""):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autores]
        self.__numeroCapitulo = numeroCapitulo
        self.__tituloCapitulo = tituloCapitulo

        self.__capitulo = {self.__tituloCapitulo: self.__numeroCapitulo}
        self.__obj_capitulos = {}
        self.__lista_capitulos = [
            Capitulo(self.__tituloCapitulo, self.__numeroCapitulo)]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @property
    def autores(self):
        return self.__autores

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Código inválido")

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Titulo inválido")

    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano
        else:
            print("Ano inválido")

    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora
        else:
            print("Editora inválida")

    def incluirAutor(self, autores: Autor):
        if isinstance(autores, Autor):
            if autores in self.__autores:
                print("autores já incluso")
            else:
                self.__autores.append(autores)
        else:
            print("autores inválido")

    def excluirAutor(self, autores: Autor):
        if isinstance(autores, Autor):
            if autores in self.__autores:
                self.__autores.remove(autores)
            else:
                print("autores não consta na lista")
        else:
            print("autores inválido")

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        for key in self.__capitulo.keys():
            if tituloCapitulo in key:
                print("Capítulo já cadastrado")
            break
        else:
            self.__capitulo[tituloCapitulo] = numeroCapitulo
            self.__obj_capitulos[tituloCapitulo] = Capitulo(
                numeroCapitulo, tituloCapitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        for key in self.__capitulo.keys():
            if tituloCapitulo in key:
                self.__capitulo.pop(tituloCapitulo)
                self.__obj_capitulos.pop(tituloCapitulo)
            else:
                print("Titulo não presente")

    def findCapituloByTitulo(self, tituloCapitulo: str) -> Capitulo:
        for key in self.__capitulo.keys():
            if key == tituloCapitulo:
                return self.__obj_capitulos[tituloCapitulo]
        else:
            print("Capitulo nao encontrado")
