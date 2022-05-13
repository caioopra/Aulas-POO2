class Editora:
    def __init__(self, codigo: int, nome: str):
        if isinstance(codigo, int) and isinstance(nome, str):       
            self.__codigo = codigo
            self.__nome = nome
        else:
            print("Valores inválidos para a editora")

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Valores inválidos para o código")

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Valores inválidos para o nome")
