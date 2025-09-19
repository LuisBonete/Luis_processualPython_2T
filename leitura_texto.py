import re
from collections import Counter

texto_digitado = input("Digite seu texto: ")


texto_limpo = re.sub(r'[^\w\s]', '', texto_digitado).lower()

palavras = texto_limpo.split()


if not palavras:
    print("Nenhum texto foi digitado.")
else:

    total_de_palavras = len(palavras)
    print(f"\nO texto tem {total_de_palavras} palavras.")

 
    palavra_mais_longa = max(palavras, key=len)
    print(f"A palavra mais longa é: '{palavra_mais_longa}'")

   
    contagem_de_palavras = Counter(palavras)
    
     
    palavra_mais_comum, frequencia = contagem_de_palavras.most_common(1)[0]
    
    print(f"A palavra que mais aparece é: '{palavra_mais_comum}', que se repete {frequencia} vezes.")
