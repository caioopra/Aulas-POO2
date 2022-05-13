from random import choice


class Baralho:
    def __init__(self, quantidadeBaralhos=1):
        self.__quantidadeBaralhos = quantidadeBaralhos
        self.__maos = {}
        self.__pilhaDescarte = []

        valoresPorNaipe = self.__quantidadeBaralhos

        naipes = ["\N{Black Spade Suit}", "\N{Black Heart Suit}",
                  "\N{Black Diamond Suit}", "\N{Black Club Suit}"]
        valores = ["1", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "J", "Q", "K"]

        baralho = []
        for naipe in naipes:
            for valor in valores:
                for _ in range(valoresPorNaipe):
                    baralho.append(f"{valor}{naipe}")
        self.__baralho = baralho

        print(self.__baralho)

    def criarMao(self, nome):
        self.__maos[nome] = ""

    def comprarCartas(self, nome, quantidade):
        for _ in range(quantidade):
            carta = choice(self.__baralho)

            self.__maos[nome] += f"{carta} "
            self.__baralho.remove(carta)

            print("Carta comprada:", carta)

    # posicao das cartas iniciando em 1
    def descartarCartas(self, nome: str, *posicoes: int):
        cartas = self.__maos[nome].split(" ")[:-1]

        nova_mao = cartas[:]
        for posicao in posicoes[::-1]:
            carta_descartada = nova_mao.pop(posicao - 1)
            self.__pilhaDescarte.append(carta_descartada)

        count = 0
        mao_temp = ""
        while count != len(nova_mao):
            mao_temp += f"{nova_mao[count]} "
            count += 1
        
        print(mao_temp)
        
    def mostrarMao(self, nome: str):
        print(self.__maos[nome])


baralho = Baralho()
# baralho2 = Baralho(2)

baralho.criarMao("Caio")
baralho.comprarCartas("Caio", 3)
baralho.mostrarMao("Caio")
baralho.descartarCartas("Caio", 1)
