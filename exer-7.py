# Função para calcular a idade em dias
def idade_em_dias():
    # Ler a idade em anos, meses e dias
    anos = int(input("Digite a idade em anos: "))
    meses = int(input("Digite a idade em meses: "))
    dias = int(input("Digite a idade em dias: "))

    # Cálculo do total de dias
    total_dias = (anos * 365) + (meses * 30) + dias

    # Exibir o resultado
    print("A idade em dias é:", total_dias)

# Chamar a função
idade_em_dias()
