import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1500, 1800, 1300, 1900, 2100, 2000]

legenda = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
plt.xticks(x, legenda)
plt.plot(x,y)
plt.show()