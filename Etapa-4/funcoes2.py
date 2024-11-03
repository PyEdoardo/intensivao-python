def maiorDeIdade(idade):
    if idade < 18:
        return "Menor de Idade!"
    elif idade == 18:
        return "Tem 18 Anos!"
    else:
        return "Maior de Idade!"
    


print(maiorDeIdade(20))

print(maiorDeIdade(40))

print(maiorDeIdade(18))

print(maiorDeIdade(15))