import pickle

from empresa import Empresa


class EmpresaDAO:
    def __init__(self, datasource="empresa.pkl"):
        self.__datasource = datasource
        self.__object_cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.datasource, "wb") as arquivo:
            pickle.dump(self.object_cache, arquivo)

    def __load(self):
        with open(self.datasource, "rb") as arquivo:
            self.object_cache = pickle.load(arquivo)

    @property
    def datasource(self):
        return self.__datasource

    @property
    def object_cache(self):
        return self.__object_cache

    @object_cache.setter
    def object_cache(self, cache):
        self.__object_cache = cache

    def add(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            self.object_cache[empresa.cnpj] = empresa
            self.__dump()
        else:
            raise TypeError

    def remove(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            self.object_cache.pop(empresa.cnpj, "Empresa nao encontrada")
            self.__dump()

    def get(self, cnpj: int):
        return self.object_cache[cnpj]

    def get_all(self):
        empresas = []
        for empresa in self.object_cache.values():
            empresas.append(empresa)
        return empresas
