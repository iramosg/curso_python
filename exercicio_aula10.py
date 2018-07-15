nome = input("Digite seu nome: ")

valid_nota = False
while valid_nota == False:
    nota1 = input("Nota da Prova 1: ")
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print("Nota inválida. Valor deve ser entre 0 e 10")
        else:
            valid_nota = True
    except:
        print("Nota inválida. Use apenas números e separe os decimais com ponto (.)")


valid_nota = False
while valid_nota == False:
    nota2 = input("Nota da Prova 2: ")
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print("Nota inválida. Valor deve ser entre 0 e 10")
        else:
            valid_nota = True
    except:
        print("Nota inválida. Use apenas números e separe os decimais com ponto (.)")


valid_faltas = False

while valid_faltas == False:
    faltas = input("Digite o total de faltas: ")
    try:
        faltas = float(faltas)
        if faltas < 0 or faltas > 20:
            print("Número de faltas inválido. Deve ser entre 0 e 20")
        else:
            valid_faltas = True
    except:
        print("Número de faltas inválido. Use apenas n´meroe e separoe os demais com ponto (.)")

media = (nota1 + nota2) / 2
presencas = (20 - faltas) / 20

if media >= 6 and presencas >= 0.7:
    resultado = 'Aprovado'
elif media < 6 and presencas < 0.7:
    resultado = 'Reprovado por média e por falta'
elif media < 6:
    resultado = 'Reprovado por média'
elif presencas < 0.7:
    resultado = 'Reprovado por faltas'
else:
    print('Erro')

print('Nome', nome)
print('Média', media)
print('Presenças',  str(presencas * 100) + '%')
print('Resultado', resultado)