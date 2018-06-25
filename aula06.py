igor = {'nome': "igor", "sobrenome": "ramos", "profissao": "programador", "filhos": ['joao', 'maria']}

print(type(igor))

igor['nome']
print(igor['nome'])
print(igor['sobrenome'])
print(igor['filhos'])

print(len(igor))

# del igor['filhos']
# print(igor)

igor['sobrenome'] = "gonçalves"

print(igor)

'sobrenome' in igor
print('sobrenome' in igor)

'idade' in igor
print('idade' in igor)

for x in igor:
    print(x)

# for x in igor:
#     print(x + ": " + igor[x])

print(igor.get('nome', 'Essa informação não consta no cadastro'))
print(igor.get('idade', 'Essa informação não consta no cadastro'))

igor['filhos'].append('jorge')

print(igor)

igor.clear()

print(igor)