#autor Guilherme Pontes Campos

p = int(input("numeros de pessoas para calcular a altura média: ")) #
pessoa = []
altura = ''

for n in range(1,p+1): 
    altura = float(input(f"altura da pessoa {n}: "))
    pessoa.append(altura)
print(f'Total: {sum(pessoa)}')
media = sum(pessoa) / len(pessoa)
print(f'Média = {media:.2f}')