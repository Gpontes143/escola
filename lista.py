def opcao1():
    nome = list('SENAC')
    print(nome)

def opcao2():
    numeros = list(range(1,16))
    print(numeros)

def opcao3():
    frutas = ['uva', 'banana', 'maça']
    print(frutas)
    frutas.append('morango')
    print(frutas)
    frutas.insert(1, 'melão')
    print(frutas)
    frutas.extend(['abacate', 'limão'])
    print(frutas)
    frutas.pop(3)
    print(frutas)
    frutas.sort()
    print(frutas)

def opcao4(): 
    notas = [5,8,7,4,2,6]
    print(notas)
    print(sorted(notas))
    print(sorted(notas, reverse = True))

opcoes = {
    '1': opcao1,
    '2': opcao2,
    '3': opcao3,
    '4': opcao4
}

opcao = input('Escolha uma opção: ')

if opcao in opcoes:
    opcoes[opcao]()
else:
    print('Opção inválida')
