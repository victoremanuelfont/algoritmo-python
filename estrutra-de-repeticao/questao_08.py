''' Escreva um programa em Python que utilize estruturas de repetição while e estruturas
condicionais if para calcular a área das figuras geométricas selecionadas pelo usuário.
O programa deve exibir um menu com as opções disponíveis para cálculo da área:
quadrado, retângulo ou triângulo. O usuário deve escolher uma opção digitando o
número correspondente ao tipo de figura geométrica desejada. Dependendo da opção
escolhida, o programa deve solicitar as dimensões necessárias para calcular a área da
figura selecionada.
a) Para o quadrado, o programa deve solicitar o lado do quadrado.
b) Para o retângulo, o programa deve solicitar a base e a altura do retângulo.
c) Para o triângulo, o programa deve solicitar a base e a altura do triângulo.
Após receber as dimensões necessárias, o programa deve calcular e exibir a área da
figura geométrica correspondente. O programa deve continuar executando até que o
usuário decida sair.'''


print("\nCalculo de Figuras geométricas")
start = input("Para entrar no programa digite ENTRAR: ")

while start == 'ENTRAR' or start == 'CONTINUAR':
    star = 0
    quadrado = 1
    print(f"\nO código da área do quadrado é: {quadrado}")
    triangulo = 2
    print(f"O código da área do triangulo é: {triangulo}")
    retangulo = 3
    print(f"O código da área do retangulo é: {retangulo}")

    entrada = int(input("\n Selecione qual numero correspondente a figura geometrica: "))


    while (entrada != quadrado) and (entrada != triangulo) and (entrada != retangulo):
        entrada = int(input("Selecione o numero CORRETO da figura geometrica: "))
        
    if entrada == quadrado:
        lado = float(input("\nQual a medida do quadrado: "))
        area = lado * lado
        print("A área do quadrado é: ", area)
    elif entrada == triangulo:
        base = float(input("\n Qual o valor da base do triangulo: "))
        altura = float(input(" Qual o valor da altura do triangulo: "))
        area = (base*altura)/2
        print("A área do triangulo é: ", area)
    elif entrada == retangulo:
        base = float(input("\n Qual o valor da base do retangulo: "))
        altura = float(input(" Qual o valor da altura do retangulo: "))
        area = (base*altura)
        print("A área do retangulo é: ", area)
        
    start = input("Para continuar no programa digite CONTINUAR: ")



        



        
        
        

        