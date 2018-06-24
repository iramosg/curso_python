prova1 = float(input("Entre com a nota da Prova 1: "))
peso1 = float(input("Qual é o peso dessa prova?: "))
prova2 = float(input("Entre com a nota da Prova 2: "))
peso2 = float(input("Qual é o peso dessa prova?: "))

media = ((prova1 * peso1) + (prova2 * peso2)) / (peso1 + peso2)

print("Sua média final é:", media)

input("Aperte Enter para sair")