frase = str(input('Digite uma frase: '))
frase_separada = frase.strip().split()
frase_formatada = ''.join(frase_separada).upper()
frase_inversa = ''

# if frase_formatada == frase_formatada[::-1]:
#     print(f'A frase é um palindromo')

# else:
#     print(f'A frase não é um palindromo')

for frase_separada in range(len(frase_formatada) -1, -1, -1):
    frase_inversa += frase_formatada[frase_separada]
print(f'O inverso de {frase_formatada} é {frase_inversa}')
if frase_inversa == frase_formatada:
    print('Temos um palindromo')
else:
    print('A frase digitada nao é um palindromo')

