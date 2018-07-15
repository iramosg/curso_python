def imc(peso, altura):
    calculo_imc = peso / (altura * altura)
    return calculo_imc


def classifica_imc(sexo, peso, altura):
    valor_imc = imc(peso, altura)
    if sexo == 'm':
        if valor_imc < 20.7:
            return 'Abaixo do peso'
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return 'Peso normal'
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return 'Marginalmente acima do peso'
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return 'Acima do peso ideal'
        elif valor_imc >= 31.1:
            return 'Obesidade'
        else:
            return 'Erro de cálculo.'

    if sexo == 'f':
        if valor_imc < 19.1:
            return 'Abaixo do peso'
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return 'Peso normal'
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return 'Marginalmente acima do peso'
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return 'Acima do peso ideal'
        elif valor_imc >= 32.3:
            return 'Obesidade'
        else:
            return 'Erro de cálculo.'


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

v_imc = str(imc(peso, altura))
c_imc = classifica_imc(sexo, peso, altura)
print('O seu IMC é:', v_imc[0:5], 'com a classificação', c_imc)
