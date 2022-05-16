from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self):
        tamanho_passo = 3
        volume_som = 3
        super().__init__(volume_som, tamanho_passo)
    
    def latir(self):
        return self.produzir_som() + "AU"