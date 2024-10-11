# Função para verificar se a pessoa pode votar
def verificar_voto(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    if idade >= 16:  # Considerando que a votação é permitida a partir dos 16 anos
        return "Você poderá votar este ano."
    else:
        return "Você não poderá votar este ano."

# Exemplo de uso
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

resultado = verificar_voto(ano_atual, ano_nascimento)
print(resultado)
