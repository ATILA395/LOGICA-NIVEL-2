# Ler o número de maçãs compradas
numero_macas = int(input("Digite o número de maçãs compradas: "))

# Definir o preço por maçã
if numero_macas < 12:
    preco_por_maca = 1.30
else:
    preco_por_maca = 1.00

# Calcular o custo total
custo_total = numero_macas * preco_por_maca

# Exibir o custo total
print(f"O custo total da compra é: R$ {custo_total:.2f}")
