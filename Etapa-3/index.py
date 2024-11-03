pessoas = ["Ciclano", "Beutrano", "Fulano"]

alguem = pessoas.index("Ciclano") ##A função index permite pegar o índice da primeira ocorrência desse valor, e irá retornar o índice dentro da lista!

print(f'Índice de alguma pessoa: {alguem}')
print(f'\nAchando a pessoa pelo índice: {pessoas[alguem]}') ##Nesse caso estamos pegando o índice pela variável alguem, onde colocamos o index!

##E podemos ainda mais!

print(f'\nLista Atual: {pessoas}') ##Lista atual!

print(f'Elemento removido: {pessoas.pop(alguem)}')

print(f'\nLista após a remoção: {pessoas}') ##Lista após termos removido o Ciclano usando o pop acima.



