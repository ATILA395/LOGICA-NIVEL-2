def verificar_compra(quantidade_estoque, quantidade_maxima, quantidade_minima):
    # Calcula a quantidade média
    quantidade_media = (quantidade_maxima + quantidade_minima) / 2
    
    # Verifica se a quantidade em estoque é maior ou igual à média
    if quantidade_estoque >= quantidade_media:
        return "Não efetuar compra"
    else:
        return "Efetuar compra"

# Leitura dos dados
quantidade_estoque = int(input("Digite a quantidade atual em estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))

# Verifica se deve efetuar a compra
resultado = verificar_compra(quantidade_estoque, quantidade_maxima, quantidade_minima)

# Saída do resultado
print(resultado)
