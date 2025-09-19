lista_numeros = []

num1 = int(input("Digite 1 número aleatório: "))
num2 = int(input("Digite 1 número aleatório: "))
num3 = int(input("Digite 1 número aleatório: "))
num4 = int(input("Digite 1 número aleatório: "))
num5 = int(input("Digite 1 número aleatório: "))
num6 = int(input("Digite 1 número aleatório: "))
num7 = int(input("Digite 1 número aleatório: "))
num8 = int(input("Digite 1 número aleatório: "))
num9 = int(input("Digite 1 número aleatório: "))
num10 = int(input("Digite o seu número da chamada: "))

lista_numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

ordem = sorted(lista_numeros)
sem_repeticao = set(lista_numeros)

print(f"\nLista original: {lista_numeros}")
print(f"Lista em ordem crescente: {ordem}")
print(f"Lista sem repetição: {sem_repeticao}")
