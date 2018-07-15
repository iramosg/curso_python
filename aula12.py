import funcoes_imc as imc


print('Vamos calcular o seu IMC?')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o seu sexo (M ou F): ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F')
    else:
        valid_sexo = True

valid_peso = False

while valid_peso == False:
    peso = input('Digite o peso (Ex.: 68.5): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('Entre com um peso válido ou menor que 350kg.')
        else:
            valid_peso = True
    except:
        print('Peso inválido. Use apenas números e separe os demais com ponto (.)')

valid_altura = False

while valid_altura == False:
    altura = input('Digite a altura em metros: ')
    try:
        altura = float(altura)
        if altura <= 0 or altura > 3:
            print('Altura inválida.')
        else:
            valid_altura = True
    except:
        print('Altura inválido. Use apenas números e separe os demais com ponto (.)')

v_imc = str(imc.imc(peso, altura))
c_imc = imc.classifica_imc(sexo, peso, altura)
print('O seu IMC é:', v_imc[0:5], 'com a classificação', c_imc)