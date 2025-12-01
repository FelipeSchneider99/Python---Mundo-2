soma = contmil = menor_valor = cont = 0
barato = ''
exit_programa = False
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    valor = float(input('Valor do produto: '))
    cont += 1
    soma += valor
    if valor > 1000:
        contmil += 1
    if cont == 1 or valor < menor_valor:
        menor_valor = valor
        barato = nome
    while True:
        opcao = input('Deseja adicionar mais um produto? [S/N] ').strip().upper()
        if opcao == 'S':
            break
        elif opcao == 'N':
            exit_programa = True
            break
        else:
            print('Opção invalida.')
    if exit_programa:
        break

print(f'O total gasto na compra foi de R${soma:.2f}')
print(f'Há {contmil} produtos acima de R$1000 reais')
print(f'O produto mais barato foi {barato} que custa R${menor_valor:.2f}')