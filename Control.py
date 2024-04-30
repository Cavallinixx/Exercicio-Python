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
                          "\n5. Até Dez"           +
                          "\n6. Números  pares de até 20"        +
                          "\n7. Soma Cem "         +
                          "\n8. Múltiplos de Cinco"     +
                          "\n9. Par ou Impar?"           +
                          "\n10. Positivo, Negativo ou Zero?"+
                          "\n11. Tabuada"        +
                          "\n12. Até num"    +
                         "\n13. Números primos 1 a 20" +
                         "\n14. Verificar se o numero é primo" +
                         "\n15. Fatorial" +
                         "\n16. Fibonacci ate dez" +
                         "\n17. Diz se é da sequência de fibonacci" +
                         "\n18. Soma digitos" +
                         "\n19. Imprimir par e impar " +
                         "\n20. Numeros  primos " +
                         "\n21. " +
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
            elif (self.opcao == 5):
                print(self.exer.ateDez())
            elif (self.opcao == 6):
                print(self.exer.pares())
            elif(self.opcao == 7):
                self.coletar2()
                print(self.exer.somaCem())
            elif(self.opcao == 8):
                print(self.exer.multiplosCinco())
            elif (self.opcao == 9):
                self.coletar()
                print(self.exer.parImpar())
            elif(self.opcao == 10):
                self.coletar()
                print(self.exer.PoNeZe())
            elif(self.opcao == 11):
                self.coletar()
                print(self.exer.tabuada())
            elif (self.opcao == 12):
                self.coletar()
                print(self.exer.ateNum())
            elif (self.opcao == 13):
                self.coletar()
                print(self.exer.primosUmAVinte())
            elif(self.opcao == 14):
                print(self.exer.primos())
            elif (self.opcao == 15):
                self.coletar()
                print(self.exer.fatorial())
            elif (self.opcao == 16):
                print(self.exer.pares())
            elif (self.opcao == 17):
                self.coletar()
                print(self.exer.verificar_fibonacci())
            elif (self.opcao == 18):
                self.coletar()
                print(self.exer.somaDigitos())
            elif (self.opcao == 19):
                self.coletar()
                print(self.exer.imprimirParEImpar())
            elif (self.opcao == 20):
                self.coletar()
                print(self.exer.())
            else:
                print("Código escolhido não é valido!")