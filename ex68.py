from random import randint

print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
contador_vitoria = 0
exit_program = False
while True:
    try:
        print('-=' * 20)
        numero = int(input('Digite um valor: '))
        numero_computador = randint(1, 10)
        resultado = numero + numero_computador
        while True:
            escolha_usuario = input('Par ou Impar? [P/I] ').strip().upper()[0]
            if escolha_usuario == 'P':
                if resultado % 2 == 0:
                    print(f'Voce jogou {numero} e o computador {numero_computador}.')
                    print('VOCE GANHOU'
                          '\nVamos jogar novamente!')
                    contador_vitoria += 1
                    break
                else:
                    print('VOCE PERDEU')
                    exit_program = True
                    break
            elif escolha_usuario == 'I':
                if resultado % 2 == 1:
                    print(f'Voce jogou {numero} e o computador {numero_computador}.')
                    print('VOCE GANHOU'
                          '\nVamos jogar novamente!')
                    contador_vitoria += 1
                    break
                else:
                    print('VOCE PERDEU')
                    exit_program = True
                    break
            else:
                print('Seleção invalida')
    except ValueError:
        print('Por favor, digite um número')
    if exit_program:
        break
print(f'Voce jogou {numero} e o computador {numero_computador}.')
print('-=' * 20)
print(f'GAME OVER! Voce venceu {contador_vitoria} vez(es).')
