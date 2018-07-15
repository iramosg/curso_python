compras = ['arroz', 'feijão', 'macarrão', 'carne']

nome = 'joaquim'

#Imprime cada item da lista
for i in compras:
    print(i)

#Imprime cada letra separadamente
for i in nome:
    print(i)

#Somatório com for
vendas = [1000, 450, 300, 920, 600]
total = 0

for i in vendas:
    total += + i
    print(total)

print(total)

#For com dicionários

cores = {'verde': 'green', 'preto': 'black', 'blue': 'azul'}

for i in cores:
    print(i, ':', cores[i])

#For loop alinhado
novas_compras = [['arroz', 'feijão', 'macarrão'], ['carne', 'frango'], ['leite', 'iorgute']]
for i in novas_compras:
    for item in i:
        print(item)

#Range
for i in range(1, 11):
    print(i)

# Range - Contagem Regressiva
for i in range(1, 11):
    print(10 - i)