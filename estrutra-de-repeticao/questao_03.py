'''Escreva um programa em Python que solicite ao usuário que insira um número inteiro
não negativo. O programa deve calcular e exibir o fatorial desse número. O fatorial de
um número é o produto de todos os números inteiros positivos de 1 até o próprio
número. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.'''

numero = int (input('Digite um número não negativo: '))

while numero<0:
    numero = int (input('O número precisa ser inteiro e positivo. Digite um número não negativo: '))
    
resultado = 1
for i in range(1, numero+1):
    resultado = resultado * i

print(f"O fatorial de {numero} é: {resultado}")
    
    
''' Características do Range:
    for i in range(inicio,fim, passo =1)
    o i é o primeiro valor do inicio, quando nao tem é zero.
 
    for i in range(4):  #somente o FIM foi passado,ficaria assim:
    [0,1,2,3]  # do i=0, até a posição 4. 
    
    for i in range(1,5) #inicio e fim
    [1,2,3,4]
    
    for i in range(1,10,2) # de 1 a 9, de 2 em 2
    [1,3,5,7,9]
    
    for i in range(10,1,-2) # decremento 
    [10, 8,6,4,2] '''