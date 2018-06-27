pessoas = []
while 'joao' not in pessoas:
    nome = input('Qual o seu nome? ')
    pessoas.append(nome)
    print("Olá,", nome)

print(pessoas)