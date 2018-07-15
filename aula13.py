import math
import time

def cont_tempo():
    inicio = time.clock()
    input("Escreva seu nome: ")
    fim = time.clock()
    tempo = round(fim - inicio, 2)
    print("Você levou " + str(tempo) + ' segundos para escrever seu nome.')

print(math.ceil(3.2))

print(math.floor(3.7))

print(math.fsum([1,2,3]))

print(math.sqrt(16))

print(time.localtime())

hora = time.localtime().tm_hour
print(hora)

minuto = time.localtime().tm_min
print(minuto)

print("Transação realizada às", str(hora) + 'h e ' + str(minuto) + ' minutos.')



cont_tempo()