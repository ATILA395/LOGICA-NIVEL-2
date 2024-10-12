inicio
    ler nome
    ler altura
    ler sexo
    
    se sexo = "M" então
        peso_ideal = (72.7 * altura) - 58
    senão se sexo = "F" então
        peso_ideal = (62.1 * altura) - 44.7
    senão
        escrever "Sexo inválido!"
        parar
    fim_se
    
    escrever peso_ideal
fim

