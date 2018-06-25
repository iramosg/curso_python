cores = {"vermelho":"red", "verde": "green", "azul": "blue"}

cor = input("Digite uma cor em português: ").lower()

print(cores.get(cor, 'Essa cor não está cadastrada.'))