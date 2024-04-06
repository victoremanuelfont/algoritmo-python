'''Um aluno está estudando matemática e deseja praticar a tabuada de multiplicação. Ele
quer criar um programa em Python que exiba a tabuada de multiplicação para um
número específico fornecido pelo usuário. Além disso, ele quer que o programa
permita que o usuário escolha quantas linhas da tabuada deseja ver. Escreva um
programa em Python que utilize estruturas de repetição for e while, juntamente com
uma estrutura condicional if, para exibir a tabuada de multiplicação para um número
específico fornecido pelo usuário.
'''
print("\nTabuada")

entrada = int(input("\nDigite um número: "))
qtd_linhas = int(input("\nDigite a quantidade de linhas: "))

for i in range(qtd_linhas):
    resposta = 0
    resposta = i * qtd_linhas
    print(f" {entrada} * {i} = {resposta}")




