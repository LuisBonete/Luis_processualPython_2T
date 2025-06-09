print("Bem-vindo à calculadora de investimentos!")

# Opções de investimento com suas taxas anuais
taxas = {
    "cdi": 0.14,
    "tesouro-direto": 0.07,
    "acoes": 0.15,
    "fundos imobiliarios": 0.24
}

# Mostrar as opções
print("Opções de investimento:")
print("cdi, tesouro-direto, acoes, fundos imobiliarios")

# Escolher investimento
investimento = input("Escolha um investimento: ").lower()

# Pegar valor e tempo
valor = float(input("Digite o valor inicial (em R$): "))
meses = int(input("Digite o tempo (em meses): "))

# Calcular taxa mensal
taxa_anual = taxas[investimento]
taxa_mensal = (1 + taxa_anual) ** (1/12) - 1

# Calcular valor final
final = valor * (1 + taxa_mensal) ** meses

# Mostrar resultado
print("Valor final: R$", round(final, 2))
