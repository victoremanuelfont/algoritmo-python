'''Escreva um programa em Python que solicite ao usuário que insira uma série de
números inteiros positivos. O programa deve calcular e exibir a média desses
números. O programa deve continuar solicitando ao usuário que insira números até
que ele insira um valor negativo, momento em que o programa deve parar de solicitar
entrada e calcular a média dos números fornecidos até esse ponto.'''

numero = int(input('Digite um número: '))
contador = 0
soma = 0
while numero>0:
    contador = contador + 1
    soma = soma + numero
    numero = int(input('Digite um número: '))

media = soma/contador
print('A media dos numeros digitados é: ', media)