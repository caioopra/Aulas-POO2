class MinhaLista:
    def __init__(self, *args):
        self.__tupla = tuple(args)

    # função executada ao usar print em objetos do tipo MinhaLista
    def __str__(self):
        stringNum = ""
        
        for i in range(len(self.__tupla)):
            stringNum += str(self.__tupla[i])
        
        string = ", ".join(stringNum)   
        stringFinal = f"[{string}]"
        
        return stringFinal

    # funcao usada para definir valor de posicao especifica de MinhaLista
    def __setitem__(self, posicao, valor):
        tupla_temp = tuple()
        for i in range(posicao):
            tupla_temp += (self.__tupla[i],)

        tupla_temp += (valor,)

        for j in range(posicao + 1, len(self.__tupla)):
            tupla_temp += (self.__tupla[j],)
        
        self.__tupla = tupla_temp
        return self.__tupla
        
    def append(self, valor):
        tupla_valor = (valor,)
        self.__tupla += tupla_valor
        
    # remove o primeiro elemento com valor passado como argumento
    def remove(self, valor_remover):
        lista_tupla = MinhaLista()
        
        removido = False
        for valor in self.__tupla:
            if valor != valor_remover or removido:
                lista_tupla.append(valor)

            if valor == valor_remover:
                removido = True

        self.__tupla = lista_tupla._MinhaLista__tupla

    # TODO: terminar implementação      
    # def sort(self):
    #     copia_tupla = self.__tupla
        
    #     for i in range(len(copia_tupla)):
    #         for j in range(i + 1, len(copia_tupla)):
    #             if copia_tupla[i] > copia_tupla[j]:
    #                 valor_temporario = copia_tupla[i]
    #                 copia_tupla[i] = copia_tupla[j]
    #                 copia_tupla[j] = valor_temporario

    #     self.__tupla = copia_tupla

    #     return self.__tupla
    
    def reverse(self):
        tupla_invertida = tuple()
        
        for i in range(len(self.__tupla) - 1, -1, -1):
            tupla_invertida += (self.__tupla[i],)
            
        return tupla_invertida
    
    def pop(self, posi = -1):
        if posi == -1:
            nova_tupla = tuple()
            for i in range(len(self.__tupla) - 1):
                nova_tupla += (self.__tupla[i],)
            valor_removido = self.__tupla[posi]
            self.__tupla = nova_tupla
            
        return valor_removido

    def sum(self):
        soma = 0
        for i in range(len(self.__tupla)):
            soma += self.__tupla[i]
        
        return soma
        
            

# instancia
nova_lista = MinhaLista(1, 3, 4, 5, 5)
print(nova_lista)

# teste append
nova_lista.append(4)
print(nova_lista)

# teste remove
nova_lista.remove(4)
print(nova_lista)

nova_lista.remove(0)
print(nova_lista)

# teste de setar item da lista
nova_lista[1] = 7
print(nova_lista)

# print(nova_lista.sort())

print(nova_lista.reverse())

print(nova_lista, nova_lista.pop())

print(nova_lista.sum())