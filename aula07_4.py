idade = int(input("Digite a sua idade: "))
sexo = input("Digite o sexo M ou F: ").lower()
cidade = input("Digite sua cidade: ").lower()


if cidade == 'rj' or cidade == 'sp':
    if sexo == 'm':
        if idade < 18:
            print('Homem menor de idade, da região Sudeste')
        else:
            print('Homem maior de idade, da região Sudeste')
    elif sexo == 'f':
        if idade < 18:
            print('Mulher menor de idade, da região Sudeste')
        else:
            print('Mulher maior de idade, da região Sudeste')
    else:
        print("Erro na entrada dos dados, da região Sudeste")
else:
    print("Teste apenas para região Sudeste")