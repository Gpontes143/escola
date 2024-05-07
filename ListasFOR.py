

def opcao1():
    estados = ["SP","RJ","MG","SC"]
    for estado in estados:
        print(estado)
def opcao2():  
    p = int(input("numeros de produtos para inserir: "))
    estoque = []
    produto = ''
    for n in range(1,p+1):
        produto = int(input(f"prduto{n}/{p}: "))
        estoque.append(produto)
    print(f'Quantidade de produtos: {estoque}')
    print(f'Total: {sum(estoque)}')
    media = sum(estoque) / len(estoque)
    print(f'Média = {media:.2f}')
    
opcoes = {
    '1': opcao1,
    '2': opcao2
}

opcao = input('Escolha uma opção: ')

if opcao in opcoes:
    opcoes[opcao]()
else:
    print('Opção inválida')
