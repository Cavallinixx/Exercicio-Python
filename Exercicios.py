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

