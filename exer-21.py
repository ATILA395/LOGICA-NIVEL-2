def calcular_salario_total(horas_trabalhadas, salario_por_hora):
    horas_por_semana = 40
    semanas_no_mes = 4
    horas_normais_no_mes = horas_por_semana * semanas_no_mes

    if horas_trabalhadas > horas_normais_no_mes:
        horas_extras = horas_trabalhadas - horas_normais_no_mes
        salario_extras = horas_extras * (salario_por_hora * 1.5)
        salario_total = (horas_normais_no_mes * salario_por_hora) + salario_extras
    else:
        salario_total = horas_trabalhadas * salario_por_hora

    return salario_total

# Leitura dos dados
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o salário por hora: "))

# Cálculo do salário total
salario_total = calcular_salario_total(horas_trabalhadas, salario_por_hora)

print(f"O salário total do funcionário é: R$ {salario_total:.2f}")
