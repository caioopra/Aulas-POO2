class Capitulo:
    def __init__(self, numero: int, titulo: str):
        if isinstance(numero, int) and isinstance(titulo, str):
            self.__numero = numero
            self.__titulo = titulo
        else:
            print("Tipos de dados inválidos para o capítulo")

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def titulo(self) -> str:
        return self.__titulo

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero
        else:
            print("Valor não é inteiro")

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Valor não permitido")
        
