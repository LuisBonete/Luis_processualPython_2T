
taxas_investimento = {
    "cdi": 0.14, 
    "tesouro-direto": 0.07,
    "acoes": 0.15, 
    "fundos_imobiliarios": 0.24 
}

print("Bem-vindo à calculadora de investimentos!")
print("Opções de investimento disponíveis:")
for investimento_nome in taxas_investimento.keys():
    print(f"- {investimento_nome.replace('_', ' ').title()}") # Mostra os nomes bonitinhos

while True:
    investimento_escolhido = input("\nQual investimento você deseja fazer? (CDI, Tesouro-Direto, Acoes, Fundos_Imobiliarios): ").lower()

    if investimento_escolhido in taxas_investimento:
        break # Sai do loop se o investimento for válido
    else:
        print("Investimento inválido. Por favor, escolha uma das opções.")

while True:
    try:
        valor_inicial = float(input("Qual o valor inicial que você deseja investir? R$ "))
        if valor_inicial <= 0:
            print("O valor inicial deve ser maior que zero.")
        else:
            break
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

while True:
    try:
        tempo_meses = int(input("Por quantos meses você deseja investir? "))
        if tempo_meses <= 0:
            print("O tempo de investimento deve ser maior que zero.")
        else:
            break
    except ValueError:
        print("Tempo inválido. Por favor, digite um número inteiro.")

# Obter a taxa anual do investimento escolhido
taxa_anual = taxas_investimento[investimento_escolhido]

# Calcular a taxa mensal equivalente (assumindo juros compostos mensais)
# Fórmula: (1 + taxa_anual)^(1/12) - 1
taxa_mensal = (1 + taxa_anual)**(1/12) - 1

# Calcular o valor final do investimento
# Usando a fórmula de juros compostos: Valor_Final = Valor_Inicial * (1 + Taxa_Mensal)^Tempo_Meses
valor_final = valor_inicial * (1 + taxa_mensal)**tempo_meses

# Calcular o lucro
lucro = valor_final - valor_inicial

print(f"\n--- Resumo do seu Investimento ---")
print(f"Investimento escolhido: {investimento_escolhido.replace('_', ' ').title()}")
print(f"Valor inicial: R$ {valor_inicial:,.2f}")
print(f"Tempo de investimento: {tempo_meses} meses")
print(f"Taxa anual ({investimento_escolhido.replace('_', ' ').title()}): {taxa_anual:.2%}")
print(f"Taxa mensal equivalente: {taxa_mensal:.2%}")
print(f"Valor final estimado: R$ {valor_final:,.2f}")
print(f"Lucro estimado: R$ {lucro:,.2f}")

print("\nLembre-se: Estes são cálculos estimados. O desempenho real do investimento pode variar.")
