# Função para calcular o salário final do vendedor
def calcular_salario_vendedor():
    # Salário fixo e comissão por carro vendido
    salario_fixo = float(input("Digite o salário fixo do vendedor: "))
    comissao_por_carro = 700.00  # comissão fixa por carro vendido
    percentual_vendas = 0.05      # 5% do valor das vendas

    # Ler dados do vendedor
    numero_carros_vendidos = int(input("Digite o número de carros vendidos: "))
    valor_total_vendas = float(input("Digite o valor total das vendas: "))

    # Calcular o salário final
    comissao_total = (numero_carros_vendidos * comissao_por_carro) + (valor_total_vendas * percentual_vendas)
    salario_final = salario_fixo + comissao_total

    # Exibir o salário final do vendedor
    print(f"O salário final do vendedor é: R${salario_final:.2f}")

# Chamar a função
calcular_salario_vendedor()
