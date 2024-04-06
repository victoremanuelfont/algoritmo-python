''') Suponha que você está desenvolvendo um programa para ajudar os estudantes a
praticar tabuada. Você quer que o programa gere aleatoriamente uma multiplicação
para o usuário resolver. O programa deve pedir ao usuário para inserir a resposta e
verificar se está correta. Se estiver correta, o programa deve imprimir uma mensagem
de parabéns e gerar uma nova multiplicação. Se estiver errada, o programa deve
imprimir uma mensagem de erro e pedir ao usuário para tentar novamente.'''
import random

valor1= random.randint(1,10)
valor2= random.randint(1,10)
resposta = int(input(f"Quanto é {valor1} x {valor2}: "))
resultado = valor1 * valor2
while resposta != resultado:
    print("Resposta errada.")
    resposta = int(input(f"Quanto é {valor1} x {valor2}: "))
            
print(f"Resposta certa! A multiplicação de {valor1} x {valor2} é {resultado}")

'''Não da pra comparar variaveis de TIPOS diferentes. Resultado é INTEIRO, logo resposta precisa ser INTEIRO'''

    



