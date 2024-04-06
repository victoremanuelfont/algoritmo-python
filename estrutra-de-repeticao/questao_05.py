'''Desenvolva um programa em Python que identifique padrões em uma lista de
números fornecida pelo usuário. O programa deve solicitar ao usuário que insira uma
lista de números separados por espaço e, em seguida, identificar se existe algum
padrão nessa lista, como sequências de números repetidos, sequências de números
pares ou ímpares, de modo que, para qualquer outro padrão, uma mensagem deverá
ser enviada reportando: "Não foi possível identificar um padrão na lista.". Além disso,
utilize o método split() para dividir a entrada em uma lista de strings, que são então
convertidas em números inteiros usando list comprehension.'''

lista = []
entrada = input("Digite os numeros: ")
numeros = [int(num) for num in entrada.split()]
tamanho_da_lista = len(numeros)

cont = 0
for i in numeros: 
      
   for i in range(tamanho_da_lista):
       for j in range(i + 1, tamanho_da_lista):
           if numeros[i] == numeros[j]:
               cont = cont + 1
               
if cont >= 1:
    print("Há um padrão na sequencia")
else:
    print("Não Há um padrão na sequencia")
    
    



