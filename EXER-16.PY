# Função para calcular a média e verificar aprovação
def verificar_aprovacao(nota1, nota2):
    # Calcular a média
    media = (nota1 + nota2) / 2
    
    # Verificar se o aluno foi aprovado
    if media >= 6:
        return f"Parabéns! Você foi aprovado com uma média de {media:.1f}."
    else:
        return f"Você foi reprovado com uma média de {media:.1f}."

# Exemplo de uso
nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))

resultado = verificar_aprovacao(nota1, nota2)
print(resultado)
