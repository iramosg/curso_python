meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

alunos = ['joao', 'maria', 'pedro', 'helena']

len(meses)
print(len(meses))

len(alunos)
print(len(alunos))

print(meses[0])
print(alunos[2])

alunos[1] = 'mariah'
print(alunos)

alunos.append('igor')
print(alunos)

alunos.insert(1, 'jonny')
print(alunos)

alunos.sort()
print(alunos)

alunos.pop(0)
print(alunos)

alunos.remove('mariah')
print(alunos)

alunos2 = ['joana', 'jorge', 'matheus']

total = alunos + alunos2
print(total)

total[2]
print(total[2])

indice = 3
print(total[indice])