

nome = list('SENAC')
#print(nome)
numeros = list(range(1,16))
#print(numeros)
frutas = ['uva', 'banana', 'maça']
#print(frutas)
#adiciona um elemnto a lista
frutas.append('morango')
#print(frutas)
#adiciona um elemnto a lista na posição indicada
frutas.insert(1,'melão')
#print(frutas)
#extend addiciona itens para o final do item
frutas.extend(['abacate', 'limão'])
#print(frutas)
#pop por padrão apaga o ultimo da lista
frutas.pop(3)
#print(frutas)
#apaga um item da lista

  
notas = [5,8,7,4,2,6]
print(notas)
print(sorted(notas))
print(sorted(notas, reverse = True))
frutas.sort()
print(frutas)
