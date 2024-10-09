# Função para calcular e exibir percentuais de votos
def calcular_percentuais():
    # Ler o número total de eleitores
    total_electores = int(input("Digite o número total de eleitores: "))
    
    # Ler o número de votos
    votos_brancos = int(input("Digite o número de votos brancos: "))
    votos_nulos = int(input("Digite o número de votos nulos: "))
    votos_validos = int(input("Digite o número de votos válidos: "))

    # Calcular percentuais
    percentual_brancos = (votos_brancos / total_electores) * 100
    percentual_nulos = (votos_nulos / total_electores) * 100
    percentual_validos = (votos_validos / total_electores) * 100

    # Exibir os resultados
    print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
    print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
    print(f"Percentual de votos válidos: {percentual_validos:.2f}%")

# Chamar a função
calcular_percentuais()
