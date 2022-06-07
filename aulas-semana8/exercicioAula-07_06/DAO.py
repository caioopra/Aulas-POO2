import pickle
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    @property
    def datasource(self):
        return self.__datasource

    @property
    def cache(self):
        return self.__cache

    def __dump(self):
        with open(self.datasource, "wb") as arquivo:
            pickle.dump(self.cache, arquivo)

    def __load(self):
        with open(self.datasource, "rb") as arquivo:
            self.__cache = pickle.load(arquivo)

    def add(self, chave, objeto):
        self.cache[chave] = objeto
        self.__dump()

    def get(self, chave):
        if chave in self.cache.keys():
            return self.cache[chave]
        else:
            return "Objeto não encontrado"

    def remove(self, chave):
        self.cache.pop(chave, "Objeto não encontrado")

    def get_all(self):
        return self.cache.values()
