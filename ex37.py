# Escreva um programa que leia um numero inteiro qualquer e peça
# para o usuario escolher qual a base de conversao:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

print('CONVERSOR DE NUMEROS')
num = int(input('Qual o numero inteiro a ser convertido:'))
print('Digite 1 para binário'
      '\nDigite 2 para octal'
      '\nDigite 3 para hexadecimal')
opcao = int(input('Qual a opção desejada: '))

if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])
else:
    print('Opção invalida')