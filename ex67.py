while True:
    numero = int(input('Digite o numero que deseja ver a tabuada: '))
    if numero <= 0:
        print('\nPROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
        break
    print('-' * 20)
    for contador in range(1, 11):
        print(f'{numero} x {contador} = {numero * contador}')
    print('-' * 20)

