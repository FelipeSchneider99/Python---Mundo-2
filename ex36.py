# Escreva um programa para aprovar o emprestimo bancario para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salario
# do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode
# exceder 30% do salario ou entao o emprestimo sera negado.

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
tempo = int(input('Em quantos anos voce pretende pagar? '))
prestacao = valor / (tempo * 12)
print(f'Para pagar uma casa de R${valor:.2f} em {tempo} anos, a prestação será de R${prestacao:.2f}')

if prestacao <= salario * 0.3:
    print('Seu emprestimo foi aprovado.')
else:
    print('Seu emprestimo foi negado')
