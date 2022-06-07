from Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, codigo, nome):
        super().__init__(nome)
        self.__codigo = codigo
    
    @property
    def codigo(self):
        return self.__codigo
    