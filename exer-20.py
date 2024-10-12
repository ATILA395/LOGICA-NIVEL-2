def calcular_duracao(h_inicial, h_final):
    if h_final >= h_inicial:
        duracao = h_final - h_inicial
    else:
        duracao = 24 - h_inicial + h_final
    return duracao

# Leitura das horas
h_inicial = int(input("Digite a hora de início (0 a 23): "))
h_final = int(input("Digite a hora de fim (0 a 23): "))

# Cálculo da duração
duracao = calcular_duracao(h_inicial, h_final)

print(f"A duração do jogo é de {duracao} horas.")
