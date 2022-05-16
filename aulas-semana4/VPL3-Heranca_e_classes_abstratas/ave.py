from abc import abstractmethod
from animal import Animal


class Ave(Animal):
    @abstractmethod
    def __init__(self, tamanho_passo, altura_voo):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo
        
    @property
    def altura_voo(self):
        return self.__altura_voo
    
    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo
    
    def mover(self):
        return "ANIMAL: DESLOCOU {} VOANDO".format(self.tamanho_passo)
        
    def produzir_som(self):
        return "AVE: PRODUZ SOM: PIU"
    