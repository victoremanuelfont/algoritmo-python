'''Escreva um programa em Python que solicite ao usuário que insira uma frase. O
programa deve contar o número de vogais na frase e exibir o resultado. Observação,
não é preciso considerar a acentuação na frase, portanto, despreza a acentuação. Além
disso, utilize o método lower(). Isso é feito para garantir que o programa conte as
vogais independentemente de estarem em maiúsculas ou minúsculas. Por exemplo, se
o caractere atual for 'A', ele será convertido para 'a'. '''

texto = input('Digite uma frase: ')
texto_minusculo = texto.lower()

cont_a = cont_e = cont_i = cont_o = cont_u = 0
 
for char in texto_minusculo:
     
    if char == 'a':
         cont_a += 1
    elif char == 'e':
         cont_e += 1
    elif char == 'i':
         cont_i += 1
    elif char == 'o':
         cont_o += 1
    elif char == 'u':
         cont_u += 1
         
    soma = cont_a + cont_e + cont_i + cont_o + cont_u 
    
    print('\nA quantidade de vogais presentes na frase é: ', soma)
    print(f"\n Sendo a vogal 'a' aparecendo {cont_a} vezes ")
    print(f"\n Sendo a vogal 'e' aparecendo {cont_e} vezes ")
    print(f"\n Sendo a vogal 'i' aparecendo {cont_i} vezes ")
    print(f"\n Sendo a vogal 'o' aparecendo {cont_o} vezes ")
    print(f"\n Sendo a vogal 'u' aparecendo {cont_u} vezes ")
    
         

        
         






