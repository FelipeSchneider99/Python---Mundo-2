cont_maior = homens = cont_mulher_menor = 0
exit_program = False
print('-='*20)
print('CADASTRO DE PESSOAS')
print('-='*20)
while True:
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [F/M]: ')).strip().upper()[0]
        if sexo in 'FM':
            break
        else:
            print('Opção invalida.')
    if idade >= 18:
        cont_maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulher_menor += 1
    while True:
        opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if opcao == 'S':
            print('\nPor favor, cadastre a proxima pessoa.\n')
            break
        elif opcao == 'N':
            exit_program = True
            break
        else:
            print('Opção invalida.')
    if exit_program:
        break
print('-='*20)
print('FIM DO PROGRAMA')
print('-='*20)
print(f'Foram cadastradas {cont_maior} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastrada(s) {cont_mulher_menor} mulher(es) menores de 20 anos.')
