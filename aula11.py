
#Função sem argumento
def mensagem():
    print('Seja bem vindo!')

mensagem()

#Função com argumento
usuario = 'abacate'
def mensagem(nome):
    print('Seja bem-vindo,', nome.title() + '!')

mensagem(usuario)

#Função que calcula o IMC
def imc(peso, altura):
    valor_imc = peso / (altura * altura)
    return valor_imc

if imc(100, 1.75) > 32:
    print('Obesidade')
else:
    print('Ainda não está obeso')