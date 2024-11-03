palavras = ["banana", "maçã", "banana", "laranja", "maçã", "banana"] ##Podemos mesclar listas com dicionários para criar códigos mais complexos!
frequencia = {

}
for palavra in palavras:
    if palavra in frequencia: 
        frequencia[palavra] += 1 ##Dessa forma ele adiciona uma chave que é associado com a fruta escolhida, e o valor padrão é um nesse caso!
    else:
        frequencia[palavra] = 1

print(frequencia)

