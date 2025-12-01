print('=' * 30)
print('{:^30}'.format('BANCO SCHNEIDER'))
print('=' * 30)
valor = int(input('Digite o valor a ser sacado: R$'))
valor_total = valor
nota = 50
total_nota = 0
while True:
    if valor_total >= nota:
        valor_total = valor_total - nota
        total_nota += 1
    else:
        if total_nota > 0:
            print(f'Total de {total_nota} cédulas de R$ {nota:.2f}')
        # if cedula == 100:
        #     cedula = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        total_nota = 0
        if valor_total ==0:
            break
print('=' * 30)
print('Volte sempre.')
