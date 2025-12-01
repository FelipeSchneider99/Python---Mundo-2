# Escreva um programa que leia dois numeros inteiros e compare-os
# mostrando na tela a mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - nao existe valor maior, os dois sao iguais

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print(f'O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais.')