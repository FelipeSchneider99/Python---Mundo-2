sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida, tente novamente.')