from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()

    def coletar(self):
        self.exer.num1 = int(input("Informe o primeiro número: "))


    def coletar2(self):
        self.exer.num1 = int(input("Informe o primeiro número: "))
        self.exer.num2 = int(input("Informe o segundo número: "))

    def menu(self):
        self.opcao = int(input("----- Menu -----\n\n" +
                          "\n0. Sair"            +
                          "\n1. Somar"           +
                          "\n2. Subtrair"        +
                          "\n3. Dividir"         +
                          "\n4. Multiplicar"     +
                          "\n5. "           +
                          "\n6. "        +
                          "\n7. "         +
                          "\n8. "     +
                          "\n9. "           +
                          "\n10. Positivo, Negativo ou Zero?"+
                          "\n11. Tabuada"        +
                          "\n12. Até num"    +
                          "\nEscolha uma das opções acima:"))

    def operacao(self):
        while(self.opcao != 0):
            self.menu() #Mostrando o menu
            if(self.opcao == 0 ):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.coletar2()
                print(self.exer.somar())
            elif(self.opcao == 2):
                self.coletar2()
                print(self.exer.subtrair())
            elif (self.opcao == 3):
                self.coletar2()
                print(self.exer.dividir())
            elif (self.opcao == 4):
                self.coletar2()
                print(self.exer.multiplicar())
            elif(self.opcao == 10):
                self.coletar()
                print(self.exer.PoNeZe())
            elif(self.opcao == 11):
                self.coletar()
                print(self.exer.tabuada())
            elif (self.opcao == 12):
                self.coletar()
                print(self.exer.ateNum())
            else:
                print("Código escolhido não é valido!")