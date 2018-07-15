import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
legenda = []
repete = 8
vez = 1

print('Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO. Você terá que digitá-la' + str(repete) + ' vezes.')
input('Aperte ENTER para começar')

while vez <= repete:
    inicio = t.clock()
    input('Digite a palavra: ')
    fim = t.clock()
    tempo = round(fim - inicio, 2)
    tempos.append(tempo)
    vezes.append(vez)
    vez_str = str(vez) + 'a vez'
    legenda.append(vez_str)
    vez += 1



plt.xticks(vezes, legenda)
plt.plot(vezes, tempos)
plt.show()