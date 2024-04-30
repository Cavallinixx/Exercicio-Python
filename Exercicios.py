class Exercicios:
    def __init__(self):
        # Construtor // (pass), para usar construtor sem variável
        self.num1 = 0
        self.num2 = 0

    def somar(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def subtrair(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def dividir(self):
        if(self.num2 == 0 ):
            return "Impossivel dividir por Zero!"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

    def multiplicar(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    def ateDez(self):
        for i in range(0, 11, 1):
            print(i)

    def pares(self):
        for i in range(0, 21, 2):
            print(i)

    def somaCem(self):
       if (self.num1 > 100):
           return f"Digite um número menor que CEM!"
       if (self.num2 > 100):
           return f"Digite um número menor que CEM!"
       else:
        print(f"A soma de {self.num1} + {self.num2} = {self.num1 + self.num2}")

    def multiplosCinco(self):
        for i in range(0,51,5):
            print(i)

    def parImpar(self):
        if (self.num1 % 2 == 0):
            return f"{self.num1} é PAR!"
        else:
            return f"{self.num1} é IMPAR!"

    def PoNeZe(self):
        #Num1
        if(self.num1 > 0):
            return f"O número escolhido: {self.num1} é Positivo!"
        if(self.num1 < 0):
            return f"O número escolhido: {self.num1} é  Negativo!"
        if(self.num1 == 0):
            return f"O número escolhido: {self.num1} é Zero!"
        #Num2
        if (self.num2 > 0):
            return f"O número escolhido:{self.num2} é Positivo!"
        if (self.num2 < 0):
            return f"O número escolhido: {self.num2} é  Negativo!"
        if (self.num2 == 0):
            return f"O número escolhido: {self.num2} é Zero!"

    def tabuada(self):
        res = ""
        for i in range(0,11,1):
            res += f"{self.num1}  X  {i}  = {self.num1 * i}\n"
        return res

    def ateNum(self):
        for i in range(1, self.num1, 1):
            print(i)

    def primos(self):
        if self.num1 <= 1:
            return False
        for i in range(2, int(self.num1 ** 0.5) + 1):
            if self.num1 % i == 0:
                return f"É Primo!"
        return f"Não é Primo!"

    def primosUmAVinte(self):
        def eh_primo(numero):
            if numero <= 1:
                return False
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    return False
            return True

        primos = []
        for i in range(1, 21):
            if eh_primo(i):
                primos.append(i)
        print("Números primos de 1 a 20:", primos)

    def fatorial(self):
        if self.num1 < 0:
            return "Não é possível calcular o fatorial de um número negativo."
        else:
            fatorial = 1
            for i in range(1, self.num1 + 1):
                fatorial *= i
            return fatorial



    def verificar_fibonacci(self):
        a, b = 0, 1
        while b < self.num1:
            a, b = b, a + b
        if b == self.num1:
            print(f"{self.num1} está na sequência de Fibonacci.")
        else:
            print(f"{self.num1} não está na sequência de Fibonacci.")

    def somaDigitos(self):
        soma = 0
        while self.num1 > 0:
            digito = self.num1 % 10
            soma += digito
            self.num1 //= 10
        return soma

        resultado = somaDigitos()
        return f"A soma dos dígitos de {self.num1} é: {resultado}"

    def imprimirParEImpar(self):
        print(f"Números pares até {self.num1}:")
        for i in range(2, self.num1 + 1, 2):
            print(i)

        print(f"\nNúmeros ímpares até {self.num1}:")
        for i in range(1, self.num1 + 1, 2):
            print(i)


    def primo(numero):

        if numero <= 1:
          return False
        for i in range(2, int(numero ** 0.5) + 1):
          if numero % i == 0:
              return False
        return True

    print(f"Números primos até {num1}:")
    for i in range(2, num1 + 1):
            if primo(i):
                print(i)













