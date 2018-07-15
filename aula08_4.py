x = 0

pessoas = []
while x < 4:
    nome = input('Qual o seu nome? ')
    #Comentário no código que não atrapalha :D

    #Evitar que o nome João não seja inserido na lista
    if nome == 'joao':
        break
    pessoas.append(nome)
    print("Olá,", nome)
    x += 1

print(pessoas)