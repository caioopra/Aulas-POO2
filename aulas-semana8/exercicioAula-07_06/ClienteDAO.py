from DAO import DAO
from Cliente import Cliente


class ClienteDAO(DAO):
    def __init__(self, arquivo):
        super().__init__(arquivo)
    
    def add(self, cliente):
        if isinstance(cliente, Cliente) and isinstance(cliente.codigo, int):
            super().add(cliente.codigo, cliente)
    
    def get(self, key):
        if isinstance(key, int):
            return super().get(key)    
    
    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)
        