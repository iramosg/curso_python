nome = input("Digite seu nome: ")
nota1 = float(input("Nota da Prova 1: "))
nota2 = float(input("Nota da Prova 2: "))
faltas = int(input("Total de Faltas: "))

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