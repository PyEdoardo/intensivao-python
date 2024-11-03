import random

numeros = []

i = 0
while i < 10:
    numeros.append(random.randint(0,10))
    i = i + 1

print(f'Lista atual: {numeros}')

numeros.sort()

print(f'\nLista Crescente: {numeros}') ##Lista organizada de forma crescente. 

numeros.sort(reverse=True)

print(f'\nLista decrescente: {numeros}') ##Lista decrescente



