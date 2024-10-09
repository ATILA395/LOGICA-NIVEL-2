# Função para calcular o novo salário
def calcular_novo_salario():
    # Ler o salário atual
    salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
    
    # Ler o percentual de reajuste
    percentual_reajuste = float(input("Digite o percentual de reajuste (em %): "))
    
    # Calcular o novo salário
    novo_salario = salario_atual + (salario_atual * (percentual_reajuste / 100))
    
    # Exibir o novo salário
    print(f"O novo salário é: R${novo_salario:.2f}")

# Chamar a função
calcular_novo_salario()
