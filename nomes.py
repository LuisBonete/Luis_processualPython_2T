nome1 = input("insira o seu nome aqui: ")
nome2 = input("insira o seu nome aqui: ")
nome3 = input("insira o seu nome aqui: ")
nome4 = input("insira o seu nome aqui: ")
nome5 = input("insira o seu nome aqui: ")
nome6 = input("insira o seu nome aqui: ")
nome7 = input("insira o seu nome aqui: ")
nome8 = input("insira o seu nome aqui: ")
nome9 = input("insira o seu nome aqui: ")
nome10 = input("insira o seu nome aqui: ")

caracteres_invalidos = ["!", "@", ",", "#", "(", ")", "|", "$"]

lista = [nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome10]
lista.sort()

encontrou_invalido_geral = False

for nome_na_lista in lista:
    encontrou_invalido_no_nome = False
    for caractere_invalido in caracteres_invalidos:
        if caractere_invalido in nome_na_lista:
            print("Caracteres invalidos encontrados no nome:", nome_na_lista,)
            encontrou_invalido_no_nome = True
            encontrou_invalido_geral = True
            break
    
    if encontrou_invalido_geral:
        break

if not encontrou_invalido_geral:
    print("\nNomes na lista (ordenados) e contagem de caracteres:")
    for nome in lista:
        
        print(f"- '{nome}': {len(nome)} caracteres")
    
