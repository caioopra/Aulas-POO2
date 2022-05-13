class Sequences:
    def fibonacci(self, termos):
        print("Seq. de Fibonacci com", termos, "termos:", end=" ")
        for i in range(termos):
            print(self.calc_fibonacci(i), end=" ")
        print()
    
    
    def calc_fibonacci(self, termos):
        if termos < 0:
            return "Valor inválido"
        elif termos == 0 or termos == 1:
            return 1
        else:
            return self.calc_fibonacci(termos - 1) + self.calc_fibonacci(termos - 2)
        

    def fatorial(self, valor):
        if valor < 2:
            return 1
        else:
            return valor * self.fatorial(valor - 1)

    def encontrarPrimos(self, valor):
        print(f"Números primos até {valor}:", end=" ")

        primos = []
        
        for num in range(1, valor + 1):
            if all(num % i != 0 for i in range(2, num)):
                primos.append(num)
        return primos
                
    
    
sequencias = Sequences()
sequencias.fibonacci(5)
sequencias.fibonacci(10)

print("Fatorial 2:", sequencias.fatorial(2))
print("Fatorial 10:", sequencias.fatorial(10))

print(sequencias.encontrarPrimos(2))
print(sequencias.encontrarPrimos(10))
