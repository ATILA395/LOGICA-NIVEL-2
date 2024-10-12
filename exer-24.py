def calcular_salario_total(salario_fixo, vendas):
    # Inicializa a comissão
    if vendas <= 1500:
        comissao = vendas * 0.03  # 3% sobre vendas até R$ 1.500
    else:
        comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)  # 3% até R$ 1.500 e 5% sobre o restante

    # Salário total é a soma do salário fixo e da comissão
    salario_total = salario_fixo + comissao
    return salario_total

# Leitura dos dados
salario_fixo = float(input("Digite o salário fixo: R$ "))
vendas = float(input("Digite o valor das vendas: R$ "))

# Cálculo do salário total
salario_total = calcular_salario_total(salario_fixo, vendas)

# Saída do resultado
print(f"O salário total do vendedor é: R$ {salario_total:.2f}")
