'''Escreva um programa em Python que gere aleatoriamente um número inteiro entre 1 e
100. Em seguida, peça ao usuário para adivinhar o número. O programa deve fornecer
dicas indicando se o número fornecido pelo usuário é maior ou menor do que o
número a ser adivinhado. O jogo deve continuar até que o usuário adivinhe
corretamente o número.'''

import random

print('Advinhação\n')

aleatorio = random.randint(1,100) 

numero = int(input("Digite um número: "))
while aleatorio != numero:
    if aleatorio>numero:
        print('O número sorteado é maior')
        numero = int(input("Digite um outro número: "))
    else:
        print('O número sorteado é menor')
        numero = int(input("Digite outro número: "))
        
print('\nVocê acertou!!')
