import random
import string

nome = input("Digite seu nome: ")
letras = string.ascii_letters  
numeros = string.digits       
simbolos = string.punctuation  

caracteres_validos = letras + numeros + simbolos

senha_com_nome = nome + "".join(random.choice(caracteres_validos) for i in range(20 - len(nome)))

senha_final = ''.join(random.sample(senha_com_nome, len(senha_com_nome)))

print(f"Sua senha segura é: {senha_final}")
