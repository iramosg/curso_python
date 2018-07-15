import random

print(random.randint(0, 10))

def mega_sena():
    jogo = [];
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num in jogo:
            continue
        else:
            jogo.append(num)

    print(sorted(jogo))

mega_sena()

alunos = ['Joao', 'Pedro', 'Maria', 'Helena', 'Guilherme']
print(random.choice(alunos))

print(random.sample(alunos, 3))