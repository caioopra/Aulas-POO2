class JogoDaForca:
    def __init__(self, palavra: str):
        self.__palavra = palavra
        
        tentativasMax = 8
        self.__vidas = tentativasMax
        self.__tentativasIncorretas = 0
        
        self.__letrasCorretas = []
        self.__indiceLetrasDescobertas = []
        self.__letrasIncorretas = []
        
    def tentativa(self, letra_buscada: str):
        # percorre a palavra e busca os indices da letra da tentativa, caso esteja correta
        indices = [indice for indice, letra in enumerate(self.__palavra) if letra == letra_buscada]
        
        if indices == []:
            self.__vidas -= 1
            self.__tentativasIncorretas += 1
            self.__letrasIncorretas.append(letra_buscada)
            
            print("Letra errada! -1 vida")
        else:
            self.__letrasCorretas.append(letra_buscada)
            for i in indices:
                self.__indiceLetrasDescobertas.append(i)
                
        self.desenharForca()
        self.respostaParcial()
        
    def desenharForca(self):
        if self.__tentativasIncorretas == 0:
            print("  /------- \n  |      |\n  |\n  |\n  |\n__|__ ")
        elif self.__tentativasIncorretas == 1:
            print("  /------- \n  |      |\n  |      O\n  |\n  |\n__|__ ")
        elif self.__tentativasIncorretas == 2:
            print("  /------- \n  |      |\n  |      O\n  |      |\n  |\n__|__ ")
        elif self.__tentativasIncorretas == 3:
            print("  /------- \n  |      |\n  |      O\n  |    --|\n  |\n__|__ ")
        elif self.__tentativasIncorretas == 4:
            print("  /------- \n  |      |\n  |      O\n  |    --|--\n  |\n__|__ ")
        elif self.__tentativasIncorretas == 5:
            print("  /------- \n  |      |\n  |      O\n  |    --|--\n  |     /\n__|__ ")
        elif self.__tentativasIncorretas == 6:
            print("  /------- \n  |      |\n  |      O\n  |    --|--\n  |     / \\\n__|__ ")   
        elif self.__tentativasIncorretas == 7:
            print("  /------- \n  |      |\n  |      O\n  |    --|--\n  |    _/ \\\n__|__ ") 
        else:
            print("  /------- \n  |      |\n  |      O\n  |    --|--\n  |    _/ \\_\n__|__ ")                

    def respostaParcial(self):
        print(self.__letrasCorretas, self.__indiceLetrasDescobertas)
        # resultado = ""
        # for i in range(len(indices)):
        #     if indices[i] == 0 and len(indices) == 1:
        #         numero_espacos = " _" * (len(self.__palavra) - 1)
        #         resultado = letra_buscada + numero_espacos
        #     else:
        #         if i == 0:
        #             resultado += " _" * (int(indices[i])) + letra_buscada + ((len(self.__palavra) - 2) - indices[i]) * " _"
        #         else:
        #             qtd = (indices[i] - indices[i - 1] - 2)
        #             resultado += " _" * (qtd) + letra_buscada
        # print(resultado)
    
    

jogo = JogoDaForca("tabua")
jogo.tentativa(input("Letra: "))



# palavra

# 1 3 6

# _a_a__a

# 1 1  2

# 0 2 4 5


# teste
# 0  3 
# t__t_


# qtd = indice - indiceAnterior - 1
# se for o ultimo da lista:
# 	qtd = len(palavra) - indiceUltimo - 1
