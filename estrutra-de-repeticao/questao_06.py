
rotulos = ["gato","cachorro","passaro","gato","cachorro","passaro","gato","cachorro","passaro","passaro"]
cont_gato = cont_cachorro = cont_pass = 0

for i in rotulos:
    if i == "gato":
        cont_gato += 1
    elif i == "cachorro":
        cont_cachorro += 1
    elif i == "passaro":
        cont_pass+= 1
    
print("Ocorrências de gatos:", cont_gato)
print("Ocorrências de cachorros:", cont_cachorro)
print("Ocorrências de pássaros:", cont_pass)