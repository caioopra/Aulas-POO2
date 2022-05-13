class Polinomio:
    def __init__(self, *coeficientes):
        self.__coeficientes = coeficientes

    def __str__(self):
        polinomio = ""
        for i in range(len(self.__coeficientes)):
            polinomio += f"{str(self.__coeficientes[i])}x^{i} "
            polinomio += f"+ " if i != len(self.__coeficientes) - 1 else ""

        return polinomio

    def grauPolinomio(self):
        for i in range(len(self.__coeficientes) - 1, -1, -1):
            if self.__coeficientes[i] != 0:
                return i + 1

    def calcularValor(self, x):
        resultado = 0
        for i in range(len(self.__coeficientes)):
            # valor de cada termo = Ci * x ^ i
            coeficiente = self.__coeficientes[i]
            resultado += coeficiente * (x ** i)
            print(f"{coeficiente} * {x} ^ {i} = {coeficiente * (x ** i)}")

        return resultado

    def getCoeficientePosicao(self, posicao):
        return self.__coeficientes[posicao]


def somarPolinomios(poli1, poli2):
    grau1 = poli1.grauPolinomio()
    grau2 = poli2.grauPolinomio()

    menor_grau = min(grau1, grau2)

    soma_coeficientes = []
    for grau in range(menor_grau):
        soma_coeficientes.append(poli1.getCoeficientePosicao(grau) +
                                 poli2.getCoeficientePosicao(grau))

    maior_grau = max(grau1, grau2)
    maior_polinomio = poli1 if grau1 > grau2 else poli2

    # comeca na ultima posicao do menor polinomio e vai até o final do maior
    for i in range(maior_grau - menor_grau + 1, maior_grau):
        soma_coeficientes.append(maior_polinomio.getCoeficientePosicao(i))

    return Polinomio(*soma_coeficientes)


def multiplicarPolinomios(poli1, poli2):
    grau1 = poli1.grauPolinomio()
    grau2 = poli2.grauPolinomio()

    menor_grau = min(grau1, grau2)

    mult_coeficientes = []
    for grau in range(menor_grau):
        mult_coeficientes.append(poli1.getCoeficientePosicao(grau) *
                                 poli2.getCoeficientePosicao(grau))

    return Polinomio(*mult_coeficientes)


polinomio1 = Polinomio(2, 0, 3, 4, 8)
print("Grau:",  polinomio1.grauPolinomio())

polinomio2 = Polinomio(3, 1, 1)
print(polinomio2.calcularValor(2))

print("Poli1:", polinomio1)
print("Poli2:", polinomio2)

print("Soma:", somarPolinomios(polinomio1, polinomio2))
print("Multiplicacao:", multiplicarPolinomios(polinomio1, polinomio2))
