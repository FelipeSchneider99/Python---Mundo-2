# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista no cartao: 5% de desconto
# em ate 2x no cartao: preço normal
# 3x ou mais no cartao: 20% de juros

valor_produto = float(input('Digite o valor do produto: '))
print('FORMA DE PAGAMENTO'
      '\n[1] DINHEIRO/CHEQUE'
      '\n[2] A VISTA NO CARTAO'
      '\n[3] 2X NO CARTAO'
      '\n[4] 3X OU MAIS NO CARTAO')
print("")
opcao = int(input('QUAL A OPCAO DESEJADA: '))
print("")
if opcao == 1:
    valor_total = valor_produto - (valor_produto * 0.10)
    desconto = valor_produto - valor_total
    print(f'OPÇÃO ESCOLHIDA: DINHEIRO ou CHEQUE\n'
          f'\nVOCE RECEBEU UM DESCONTO DE R$ {desconto:.2f}'
          f'\nVALOR FINAL DO PRODUTO: R${valor_total:.2f}')
elif opcao == 2:
    valor_total = valor_produto - (valor_produto * 0.05)
    desconto = valor_produto - valor_total
    print(f'OPÇÃO ESCOLHIDA: A VISTA NO CARTAO\n'
          f'\nVOCE RECEBEU UM DESCONTO DE R$ {desconto:.2f}'
          f'\nVALOR FINAL DO PRODUTO: R${valor_total:.2f}')
elif opcao == 3:
    print(f'OPÇÃO ESCOLHIDA: 2X NO CARTAO'
          f'\nSUA COMPRA SERA PARCELADA EM 2X DE R${valor_produto / 2:.2f } SEM JUROS'
          f'\nVALOR FINAL DO PRODUTO: R${valor_produto:.2f}')
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    valor_total = valor_produto + (valor_produto * 0.20)
    print(f'OPÇÃO ESCOLHIDA: 3X OU MAIS NO CARTAO'
          f'\nSUA COMPRA SERA PARCELADA EM {parcela}X DE R${valor_total / parcela:.2f} COM JUROS'
          f'\nVALOR FINAL DO PRODUTO: R${valor_total:.2f}')
else:
    print('OPÇÃO INVALIDA')
