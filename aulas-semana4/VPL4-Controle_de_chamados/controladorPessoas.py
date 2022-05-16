from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        if self.__clientes == []:
            novoCliente = Cliente(nome, codigo)
            self.__clientes.append(novoCliente)
            return novoCliente
        else:
            for cliente in self.clientes:
                if not (cliente.codigo == codigo):
                    novoCliente = Cliente(nome, codigo)
                    self.__clientes.append(novoCliente)
                    return novoCliente
                else:
                    print("Cliente já cadastrado")

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        if self.__tecnicos == []:
            novoTecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(novoTecnico)
            return novoTecnico
        else: 
            for tecnico in self.tecnicos:
                if not (tecnico.codigo == codigo):
                    novoTecnico = Tecnico(nome, codigo)
                    self.__tecnicos.append(novoTecnico)
                    return novoTecnico
                else:
                    print("Técnico já cadastrado")
