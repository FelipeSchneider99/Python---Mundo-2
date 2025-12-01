opcao = 0
print('-=' * 10)
print('MENU')
print('-=' * 10)

while opcao != 5:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('')
    print('[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] Novos números'
          '\n[5] Sair')
    print('')
    opcao = int(input('Digite uma opção: '))
    print('')
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma dos dois valores ficou: {soma}')
        break
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação dos dois valores ficou: {multiplicacao}')
        break
    elif opcao == 3:
        maior = max(n1, n2)
        print(f'O maior numero entre {n1} e {n2} é: {maior}')
        break
    elif opcao == 4:
        print('Por favor, insira os novos numeros desejados.')
        print('')
    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida, tente novamente.')
