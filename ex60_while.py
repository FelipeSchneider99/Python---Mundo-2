print('FATORIAL WHILE')
fatorial = 1
n = int(input('Digite um numero: '))
numero_escolhido = n
if n == 0:
    print ('O fatorial de 0 é 1')
elif n < 0:
    print('Não existe fatorial de números negativos')
else:
    while n > 0:
        fatorial = fatorial * n
        n -= 1
print(f'O fatorial de {numero_escolhido}! é igual a {fatorial}')

