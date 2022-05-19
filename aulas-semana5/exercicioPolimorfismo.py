from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, nome, altura, comprimento, carga, velocidade):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade
    
    def descricaoGenerica(self):
        return f"{self.__nome}, possui {self.__altura} metros de altura e {self.__comprimento} de comprimento. Com {self.__velocidade}km/h de velocidade maxima e carga maxima de {self.__carga} toneladas."


class TransporteAreo(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, autonomia, envergadura):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura
    
    def descricao(self) -> str:
        return super().descricaoGenerica() + f"Possui {self.__autonomia} km de autonomia e {self.__envergadura} metros de envergadura."
        


class TransporteTerrestre(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, motor, rodas):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas

    def descricao(self) -> str:
        return super().descricaoGenerica() + f"Possui motor {self.__motor} e rodas {self.__rodas}."



class TransporteAquatico(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, boca, calado):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    def descricao(self) -> str:
        return super().descricaoGenerica() + f"Possui {self.__boca} metros de boca e {self.__calado} metros de calado."



class Catalogo:
    def __init__(self):
        self.__listaTransportes = []

    def inserirTransporte(self, transporte: Transporte):
        if isinstance(transporte, Transporte):
            self.__listaTransportes.append(transporte)
        else:
            print("Transporte inválido")
    
    def apresentacao(self):
        for transporte in self.__listaTransportes:
            print(transporte.descricao())


transporte = TransporteAquatico("barco", 4, 10, 5, 20, 10, 20)
print(transporte.descricao())

catalogo = Catalogo()
catalogo.inserirTransporte(transporte)
catalogo.apresentacao()