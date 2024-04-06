'''Um desenvolvedor está criando um sistema de registro de usuários para um site e
deseja garantir que cada endereço de e-mail fornecido pelos usuários seja único. Ele
decidiu implementar uma verificação para garantir que nenhum endereço de e-mail
duplicado seja cadastrado. Escreva um programa em Python que solicite ao usuário
um endereço de e-mail e verifique se esse endereço já foi cadastrado anteriormente. O
programa deve manter uma lista de endereços de e-mail já cadastrados e usar um loop
para verificar se o endereço fornecido pelo usuário já existe na lista. Se o endereço já
estiver na lista, o programa deve exibir uma mensagem informando que o endereço de
e-mail já está em uso. Caso contrário, o programa deve adicionar o novo endereço à
lista e exibir uma mensagem informando que o endereço de e-mail foi registrado com
sucesso. Obs: utilize o método lower() que converte todos os caracteres de uma string
em letras minúscula. Também utilize o método append(), usado em Python para
adicionar um elemento ao final de uma lista. Ele modifica a lista original, adicionando
o novo elemento como seu último item'''

print("Cadastre 5 email: ")

lista = []
for i in range(5):
    email = input("\nDigite o email: ").lower()
    while email in lista:
        email = input("\nJá tem esse email. Digite outro o email: ").lower()  
    lista.append(email)
    
print("Email Cadastrados: ", lista)
    
