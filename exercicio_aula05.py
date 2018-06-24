meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

data_nasc = input("Digite sua data de nascimento no formato DD-MM-AAAA: ")
mes = int(data_nasc[3:5]) - 1
print("Você nasceu no mês:", meses[mes])


