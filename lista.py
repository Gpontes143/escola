

nome = list('SENAC')
print(nome)

numeros = list(range(1,16))

print(numeros)

frutas = ['uva', 'banana', 'maça']
print(frutas)

#adiciona um elemnto a lista
frutas.append('morango')

print(frutas)

#adiciona um elemnto a lista na posição indicada
frutas.insert(1,'melão')

print(frutas)

#extend addiciona itens para o final do item
frutas.extend(['abacate', 'limão'])
print(frutas)
#pop por padrão apaga o ultimo da lista

frutas.pop()

print(frutas)
