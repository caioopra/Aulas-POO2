class Imc:
    def __init__(self, peso, altura):
        self.__altura = float(altura)
        self.__peso = float(peso)

    def calcularIMC(self):
        imc = self.__peso / self.__altura**2

        return round(imc, 2)

    def classificarIMC(self, valor):
        if valor < 18.5:
            return ", abaixo do peso normal"
        elif valor < 25:
            return ", peso normal"
        elif valor < 30:
            return ", excesso de peso"
        elif valor < 35:
            return ", obesidade classe I"
        elif valor < 40:
            return ", obesidade classe II"
        else:
            return ", obesidade classe III"
