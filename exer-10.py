# Função para calcular o custo final do carro
def calcular_custo_final():
    # Percentuais
    percentual_distribuidor = 0.28  # 28%
    percentual_impostos = 0.45        # 45%

    # Ler o custo de fábrica
    custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

    # Calcular o custo final
    custo_distribuidor = custo_fabrica * percentual_distribuidor
    custo_impostos = custo_fabrica * percentual_impostos
    custo_final = custo_fabrica + custo_distribuidor + custo_impostos

    # Exibir o custo final ao consumidor
    print(f"O custo final ao consumidor é: R${custo_final:.2f}")

# Chamar a função
calcular_custo_final()
