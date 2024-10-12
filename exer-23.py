def calcular_salario_total(salario_fixo, vendas):
    # Comissão
    if vendas <= 1500:
        comissao = vendas * 0.03
    else:
        comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)
    
    # Salário total
    salario_total = salario_fixo + comissao
    return salario_total

# Leitura dos dados
salario_fixo = float(input("Digite o salário fixo: R$ "))
vendas = float(input("Digite o valor das vendas: R$ "))

# Cálculo do salário total
salario_total = calcular_salario_total(salario_fixo, vendas)

# Saída do resultado
print(f"O salário total do vendedor é: R$ {salario_total:.2f}")
