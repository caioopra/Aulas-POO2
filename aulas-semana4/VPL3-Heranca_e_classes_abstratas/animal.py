from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, tamanhoPasso: int):
        self.__tamanhoPasso = tamanhoPasso

    @abstractmethod
    def produzir_som(self):
        pass

    @property
    def tamanhoPasso(self):
        return self.__tamanhoPasso

    @tamanhoPasso.setter
    def tamanhoPasso(self, tamanhoPasso: int) -> int:
        self.__tamanhoPasso = tamanhoPasso

    def mover(self):
        print("ANIMAL:DESLOCOU", self.tamanhoPasso)
