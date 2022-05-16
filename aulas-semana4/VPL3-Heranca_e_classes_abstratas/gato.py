from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self):
        self.__tamanho_passo = 2
        self.__volume_som = 2
        super().__init__(self.__volume_som, self.__tamanho_passo)
    
    def miar(self):
        return self.produzir_som() + "MIAU"